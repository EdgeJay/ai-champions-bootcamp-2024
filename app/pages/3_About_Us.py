import streamlit as st
import page

class AboutUs(page.PageTemplate):
    def render(self):
        if super().render():
            return True
        return False

aboutUs = AboutUs('About Us')
aboutUs.render()
