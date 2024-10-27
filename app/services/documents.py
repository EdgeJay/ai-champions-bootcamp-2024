import requests
import uuid
import env
from bs4 import BeautifulSoup
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

CHROMA_COLLECTION_NAME = 'mse_policies_collection'

class Document:
    id: str
    url: str
    is_loaded: bool

    def __init__(self, id, url):
        self.id = id
        self.url = url
        self.is_loaded = False

# Service for loading documents from web pages, local files, etc and
# store into database
class DocumentStorageService:
    doc_splitter_chunk_size: int
    embeddings: OpenAIEmbeddings
    debug_mode: bool

    def __init__(self, embeddings, doc_splitter_chunk_size=1000, debug_mode=False):
        self.embeddings = embeddings
        self.doc_splitter_chunk_size = doc_splitter_chunk_size
        self.debug_mode = debug_mode

    def get_chroma_client(self):
        return Chroma(
            collection_name=CHROMA_COLLECTION_NAME,
            persist_directory=env.get_database_path(),
            embedding_function=self.embeddings
        )

    def retrieve_html(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.text.replace('\n', '')
        unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, text))
        print(f'Document ({unique_id}) loaded from {url}')
        return [unique_id, text]
    
    def split_text(self, text, metadata=None):
        # split document content into chunks
        text_splitter = CharacterTextSplitter(chunk_size=self.doc_splitter_chunk_size, chunk_overlap=0)
        docs = []
        if metadata != None:
            docs = text_splitter.create_documents([text], [metadata]) # returns List[Document]
        else:
            docs = text_splitter.create_documents([text]) # returns List[Document]
        return docs

    def load_and_store_html_document(self, id, url, force_reload=False):
        # get chromadb client
        chroma_client = self.get_chroma_client()

        # get ids of existing docs to reduce need to add
        # documents into database repeatedly
        doc_ids = chroma_client.get()['ids']
        
        # download html document
        unique_id, text = self.retrieve_html(url)

        if not force_reload and unique_id in doc_ids:
            print(f'Document {unique_id} already in database')
        else:
            docs = self.split_text(text, {'id': id, 'url': url})
            chroma_client.add_documents(
                documents=docs,
                ids=[unique_id]
            )
        return True
    
    def query_document(self, doc_id, query_text):
        # get chromadb client
        chroma_client = self.get_chroma_client()

        # Create retriever interface
        retriever = chroma_client.as_retriever(
            search_kwargs={'filter': {'id': doc_id}}
        )

        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(api_key=env.get_openai_key(), model=env.llm_model()),
            retriever=retriever
        )

        return qa_chain.invoke(query_text)
    
    def query_documents(self, query_text):
        # get chromadb client
        chroma_client = self.get_chroma_client()

        # Create retriever interface
        retriever = chroma_client.as_retriever(
            search_kwargs={'k': 5}
        )

        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(api_key=env.get_openai_key(), model=env.llm_model()),
            retriever=retriever
        )

        return qa_chain.invoke(query_text)
