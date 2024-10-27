import streamlit as st
import page

class Methodologies(page.PageTemplate):
    def render(self):
        if super().render():
            return True
        return False

methodologies = Methodologies('Methodologies')
methodologies.render()
