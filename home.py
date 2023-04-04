from pathlib import Path
import streamlit as st
from PIL import Image

from src.init import init_page

init_page()
HOME_DIR = st.session_state['home_dir']

st.title('Currently opening an event')
home_image = Image.open(HOME_DIR / 'asset/SI_Data_Analysis_Challenge_1.png')
st.image(home_image)