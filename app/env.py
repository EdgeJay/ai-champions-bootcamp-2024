import os

def is_debug_mode():
    return os.environ['DEBUG_MODE'] == '1'

def get_openai_key():
    return os.environ['OPENAI_KEY']

def llm_model():
    return os.environ['LLM_MODEL']
