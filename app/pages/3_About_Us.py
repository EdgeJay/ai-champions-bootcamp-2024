import streamlit as st
import page
import utils

class AboutUs(page.PageTemplate):
    def render(self):
        if super().render():
            md = utils.read_file('./app/pages/3_About_Us.md')
            st.markdown(md)
            return True
        return False

aboutUs = AboutUs('About Us')
aboutUs.render()
