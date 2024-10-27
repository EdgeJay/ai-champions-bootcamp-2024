import streamlit as st
import page
import utils

class Methodologies(page.PageTemplate):
    def render(self):
        if super().render():
            md = utils.read_file('./app/pages/4_Methodologies.md')
            st.markdown(md)
            return True
        return False

methodologies = Methodologies('Methodologies')
methodologies.render()
