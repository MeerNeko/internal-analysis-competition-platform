import streamlit as st
from PIL import Image

def main():
    st.title('Currently opening an event')
    home_image = Image.open('./asset/SI_Data_Analysis_Challenge_1.png')
    st.image(home_image)

if __name__=='__main__':
    main()