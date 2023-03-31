import tomllib
import datetime
import streamlit as st 
import pandas as pd 
from PIL import Image

from utils import read_mdfile

header_image = Image.open('./asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

description = read_mdfile('./asset/leaderboard_description.md')
st.markdown(description)

with open('config/config.toml', 'rb') as f:
    config = tomllib.load(f)
    app_config = config['app']

df_pub = pd.read_csv('asset/public_leaderboard.csv')
df_lb_pub = df_pub.groupby('user_name').min()
asc = True if app_config["asc"] else False
df_lb_pub = df_lb_pub.sort_values(['score', 'date'], ascending=asc)
st.dataframe(df_lb_pub)

dt_now = datetime.date.today()
if dt_now > app_config['end_date']:
    df_pri = pd.read_csv('asset/private_leaderboard.csv')
    df_lb_pri = df_pri.groupby('user_name').min()
    df_lb_pri = df_lb_pri.sort_values(['score', 'date'], ascending=asc)
    st.header("Private")
    st.dataframe(df_lb_pri)


