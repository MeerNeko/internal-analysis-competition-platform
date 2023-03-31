import streamlit as st 
from PIL import Image

from utils import read_mdfile

header_image = Image.open('./asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

description = read_mdfile('./asset/description.md')
st.markdown(description)

