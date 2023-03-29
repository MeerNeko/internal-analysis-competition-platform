import streamlit as st 
import pandas as pd 

st.subheader("Leader Board")

df = pd.read_csv('asset/leader_board.csv')

# FIXME: Configからmin or max指定できるように
df_lb = df.groupby('user_name').min()
st.write(df_lb)

