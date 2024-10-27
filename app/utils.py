import streamlit as st
import hmac
import const
import policy
import env
from services import documents

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

def check_app_password():
    if not env.app_password_protection_enabled():
        return True

    # Returns `True` if the user had the correct password.
    def password_entered():
        # Checks whether a password entered by the user is correct.
        if hmac.compare_digest(st.session_state['password'], st.secrets['password']):  
            st.session_state['password_correct'] = True  
            del st.session_state['password']  # Don't store the password.  
        else:  
            st.session_state['password_correct'] = False  
    
    # Return True if the passward is validated.  
    if st.session_state.get('password_correct', False):
        return True
    
    # Show input for password.  
    st.text_input(  
        "Password", type="password", on_change=password_entered, key="password"  
    )  
    
    if "password_correct" in st.session_state:  
        st.error("😕 Password incorrect")  
    
    return False

def read_file(path):
    file = open(path, 'r')
    return file.read()
    