import os
import streamlit as st 

from utils import read_mdfile

data_description = read_mdfile('./asset/data_description.md')

st.markdown(data_description)

DATA_PATH = "./asset/data.zip"
with open(DATA_PATH, "rb") as file:
    btn = st.download_button(
            label="Download all data",
            data=file,
            file_name="data.zip"
          )
data_size = os.path.getsize(DATA_PATH)
st.write(f'File size: {data_size/1024:.2f} kB')

update_info = read_mdfile('./asset/data_announcement.md')
st.markdown(update_info)