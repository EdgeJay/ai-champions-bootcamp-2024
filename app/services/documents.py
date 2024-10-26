import streamlit as st
import requests
from bs4 import BeautifulSoup

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
    debug_mode: bool

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def is_document_loaded(self, id):
        return st.session_state['documents'][id].is_loaded

    def load_and_store_html_document(self, id, url, force_reload=False):
        if not force_reload and self.is_document_loaded(id):
            print(f'Document ({id}) already loaded')
            return True
        
        # reset loaded state
        st.session_state['documents'][id].is_loaded = False

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        final_text = soup.text.replace('\n', '')

        if self.debug_mode:
            print(final_text)

        print(f'Document ({id}) loaded')

        # save loaded state
        st.session_state['documents'][id].is_loaded = True

        return True