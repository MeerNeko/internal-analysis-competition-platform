import streamlit as st 

from utils import read_mdfile

description = read_mdfile('./asset/description.md')
st.markdown(description)

