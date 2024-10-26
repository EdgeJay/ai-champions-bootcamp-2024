import os
import streamlit as st
import certifi
import page

# add path to certifi pem file to avoid SSL verification errors
# when making HTTP requests to external sources
os.environ['REQUESTS_CA_BUNDLE'] = str(certifi.where())

class Home(page.PageTemplate):
    def render(self):
        super().render()
        
        st.text('Hi, what would you like to learn about today?')

        nav_col1, nav_col2 = st.columns(2)

        nav_policy_button = None
        nav_sustain_button = None

        with nav_col1:
            nav_policy_button = st.button('Policies AMA', use_container_width=True)
        with nav_col2:
            nav_sustain_button = st.button('Sustainability Facts', use_container_width=True)

        if nav_policy_button:
            st.switch_page("pages/1_Policies_AMA.py")
        elif nav_sustain_button:
            st.switch_page("pages/2_Sustainability_Facts.py")

home = Home('MSE Policies')
home.render()
