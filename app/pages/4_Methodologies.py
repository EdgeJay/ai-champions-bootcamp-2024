import streamlit as st
import page

class Methodologies(page.PageTemplate):
    def render(self):
        super().render()

methodologies = Methodologies('Methodologies')
methodologies.render()
