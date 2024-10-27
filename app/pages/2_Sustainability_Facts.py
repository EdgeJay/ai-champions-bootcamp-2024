import streamlit as st
import page

class SustainabilityFacts(page.PageTemplate):
    def render(self):
        if super().render():
            st.text("Today's fun fact")
            return True
        return False

sustainabilityFacts = SustainabilityFacts('Sustainability Facts')
sustainabilityFacts.render()
