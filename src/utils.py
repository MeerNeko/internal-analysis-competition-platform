import streamlit as st

from src.init import init_page

def get_config():
    if 'config' not in st.session_state:
        init_page()
    return st.session_state['config']

def read_mdfile(mdfile_path:str) -> str:
    lines = []
    with open(mdfile_path, encoding='utf-8') as f:
        lines = f.readlines()
    markdown = ''.join(lines)

    return markdown