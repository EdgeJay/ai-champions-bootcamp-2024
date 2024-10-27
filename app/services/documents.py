import streamlit as st
import requests
import uuid
import env
from pathlib import Path
from bs4 import BeautifulSoup
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

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

    def retrieve_html(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.text.replace('\n', '')
        unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, text))
        print(f'Document ({unique_id}) loaded from {url}')
        return [unique_id, text]
    
    def split_text(self, text):
        # split document content into chunks
        text_splitter = CharacterTextSplitter(chunk_size=self.doc_splitter_chunk_size, chunk_overlap=0)
        return text_splitter.create_documents([text]) # returns List[Document]

    def load_and_store_html_document(self, url):
        # get chromadb client
        chroma_client = Chroma(
            collection_name=CHROMA_COLLECTION_NAME,
            persist_directory=env.get_database_path(),
            embedding_function=self.embeddings
        )

        # get ids of existing docs to reduce need to add
        # documents into database repeatedly
        doc_ids = chroma_client.get()['ids']
        
        # download html document
        unique_id, text = self.retrieve_html(url)

        if unique_id not in doc_ids:
            docs = self.split_text(text)

            chroma_client.add_documents(
                documents=docs,
                ids=[unique_id]
            )
        else:
            print(f'Document {unique_id} already in database')

        return True