import streamlit as st 
from PIL import Image

from src.utils import read_mdfile

HOME_DIR = st.session_state['home_dir']

header_image = Image.open(HOME_DIR / 'asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

description = read_mdfile(HOME_DIR / 'asset/description.md')
st.markdown(description)

