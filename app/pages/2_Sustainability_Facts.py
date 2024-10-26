import streamlit as st
import page

class SustainabilityFacts(page.PageTemplate):
    def render(self):
        super().render()
        st.text("Today's fun fact")

sustainabilityFacts = SustainabilityFacts('Sustainability Facts')
sustainabilityFacts.render()
