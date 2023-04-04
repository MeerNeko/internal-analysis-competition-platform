import os
import streamlit as st 
from PIL import Image

from src.utils import read_mdfile

HOME_DIR = st.session_state['home_dir']

header_image = Image.open(HOME_DIR / 'asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

data_description = read_mdfile(HOME_DIR / 'asset/data_description.md')

st.markdown(data_description)

DATA_PATH = HOME_DIR / 'asset/data.zip'
with open(DATA_PATH, 'rb') as file:
    btn = st.download_button(
            label='Download all data',
            data=file,
            file_name='data.zip'
          )
data_size = os.path.getsize(DATA_PATH)
st.write(f'File size: {data_size/1024:.2f} kB')

update_info = read_mdfile(HOME_DIR / 'asset/data_announcement.md')
st.markdown(update_info)