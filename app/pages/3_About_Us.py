import streamlit as st
import page

class AboutUs(page.PageTemplate):
    def render(self):
        super().render()

aboutUs = AboutUs('About Us')
aboutUs.render()
