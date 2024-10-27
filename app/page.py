import streamlit as st
import utils

class PageTemplate:
    page_title: str
    title: str
    show_disclaimer: bool

    def __init__(self, page_title, title=None, show_disclaimer=True):
        utils.initialise_session()
        self.page_title = page_title
        if title != None:
            self.title = title
        else:
            self.title = page_title
        self.show_disclaimer = show_disclaimer
    
    def render(self):
        st.set_page_config(page_title=self.title)
        st.title(self.title)

        if not utils.check_app_password():
            return False

        # Disclaimer
        if self.show_disclaimer:
            with st.expander('IMPORTANT NOTICE', expanded=False):
                st.markdown("""
This web application is a prototype developed for **educational purposes only**. The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**

Always consult with qualified professionals for accurate and personalized advice.
""")
        return True