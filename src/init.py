import tomllib
from pathlib import Path
import streamlit as st

def init_page():
    config_path = Path('config/config.toml')
    with open(config_path, 'rb') as f:
        config = tomllib.load(f)
    st.session_state['config'] = config
    st.session_state['home_dir'] = Path.cwd()
