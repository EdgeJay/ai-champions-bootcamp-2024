import streamlit as st
import const

def initialise_session():
    if 'selected_policy' not in st.session_state:
        st.session_state['selected_policy'] = const.NAV_POLICY_CLIMATE

def get_selected_policy():
    return st.session_state['selected_policy']

def set_selected_policy(policy):
    st.session_state['selected_policy'] = policy