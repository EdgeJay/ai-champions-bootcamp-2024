import streamlit as st
import utils

USER_ROLE = 'user'
ASSISTANT_ROLE = 'assistant'

class ChatMessage:
    role: str
    content: str

    def __init__(self, role, content):
        self.role = role
        self.content = content

def save_chat_message(chat_id, role, content):
    if chat_id not in st.session_state['chat_messages']:
        st.session_state['chat_messages'][chat_id] = []
    st.session_state['chat_messages'][chat_id].append(ChatMessage(role, content))

def get_chat_messages(chat_id):
    if chat_id in st.session_state['chat_messages']:
        return st.session_state['chat_messages'][chat_id]
    return []

class ChatContainer:
    input_prompt: str
    chat_callback: any

    def __init__(self, input_prompt='Say something', chat_callback=None):
        self.input_prompt = input_prompt
        self.chat_callback = chat_callback
    
    def render(self):
        chat_id = utils.get_selected_policy_nav()
        
        messages = get_chat_messages(chat_id)
        for m in messages:
            with st.chat_message(m.role):
                st.markdown(m.content)
        
        if user_input := st.chat_input(self.input_prompt):
            st.chat_message(USER_ROLE).markdown(user_input)
            save_chat_message(chat_id, USER_ROLE, user_input)
            
            if self.chat_callback != None:
                self.chat_callback(USER_ROLE, user_input)
    
    def add_assistant_message(content):
        chat_id = utils.get_selected_policy_nav()
        save_chat_message(chat_id, ASSISTANT_ROLE, content)
