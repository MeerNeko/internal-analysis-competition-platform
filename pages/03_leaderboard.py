import tomllib
import datetime
import streamlit as st 
import pandas as pd 
from PIL import Image

from src.utils import get_config, read_mdfile

config = get_config()
HOME_DIR = st.session_state['home_dir']

header_image = Image.open(HOME_DIR / 'asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

description = read_mdfile(HOME_DIR / 'asset/leaderboard_description.md')
st.markdown(description)


df_pub = pd.read_csv(HOME_DIR / 'asset/public_leaderboard.csv')
df_lb_pub = df_pub.groupby('user_name').min()
asc = True if config['app']['asc'] else False
df_lb_pub = df_lb_pub.sort_values(['score', 'date'], ascending=asc)
st.dataframe(df_lb_pub)

dt_now = datetime.date.today()
if dt_now > config['app']['end_date']:
    df_pri = pd.read_csv(HOME_DIR / 'asset/private_leaderboard.csv')
    df_lb_pri = df_pri.groupby('user_name').min()
    df_lb_pri = df_lb_pri.sort_values(['score', 'date'], ascending=asc)
    st.header('Private')
    st.dataframe(df_lb_pri)


