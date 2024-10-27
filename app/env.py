import os

def is_debug_mode():
    return os.environ['DEBUG_MODE'] == '1'

def get_database_path():
    return os.environ['DATABASE_PATH']

def get_openai_key():
    return os.environ['OPENAI_KEY']

def llm_model():
    return os.environ['LLM_MODEL']

def force_reload_documents():
    return os.environ['FORCE_RELOAD_DOCUMENTS'] == '1'
