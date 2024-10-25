import streamlit as st
import const
import policy

def initialise_session():
    if 'selected_policy' not in st.session_state:
        st.session_state['selected_policy'] = const.NAV_POLICY_CLIMATE
    # chat messages
    if 'chat_messages' not in st.session_state:
        st.session_state['chat_messages'] = {}

def get_selected_policy():
    return next((p for p in policy.all_policies if p.nav_id == get_selected_policy_nav()), None)

def get_selected_policy_nav():
    return st.session_state['selected_policy']

def set_selected_policy_nav(policy_nav_id):
    st.session_state['selected_policy'] = policy_nav_id