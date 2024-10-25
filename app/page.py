import streamlit as st
import utils

class PageTemplate:
    page_title: str
    title: str

    def __init__(self, page_title, title=None):
        utils.initialise_session()
        self.page_title = page_title
        if title != None:
            self.title = title
        else:
            self.title = page_title
    
    def render(self):
        st.set_page_config(page_title=self.title)
        st.title(self.title)