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
df_lb_pub['last'] = df_pub.groupby('user_name').max()['date']
df_lb_pub = df_lb_pub.drop(['date'], axis=1)
df_lb_pub['entries'] = df_pub.groupby('user_name').count()['score']
asc = True if config['app']['asc'] else False
df_lb_pub = df_lb_pub.sort_values(['score', 'last'], ascending=asc)
df_lb_pub['rank'] = [i for i in range(1, len(df_lb_pub)+1)]
df_lb_pub = df_lb_pub.df.reset_index().set_index('rank')
st.dataframe(df_lb_pub)

dt_now = datetime.date.today()
if dt_now > config['app']['end_date']:
    df_pri = pd.read_csv(HOME_DIR / 'asset/private_leaderboard.csv')
    df_lb_pri = df_pri.groupby('user_name').min()
    df_lb_pri = df_lb_pri.sort_values(['score', 'date'], ascending=asc)
    st.header('Private')
    st.dataframe(df_lb_pri)


#%% 
import pandas as pd 


# df_pub = pd.read_csv('/Users/t.ito/Documents/project/internal-analysis-competition-platform/asset/public_leaderboard.csv')
# df_lb_pub = df_pub.groupby('user_name').min()
# df_lb_pub['last'] = df_pub.groupby('user_name').max()['date']
# df_lb_pub = df_lb_pub.drop(['date'], axis=1)
# df_lb_pub['entries'] = df_pub.groupby('user_name').count()['score']
# df_lb_pub = df_lb_pub.sort_values(['score', 'last'], ascending=True)
# df_lb_pub

df_pub = pd.read_csv('../asset/public_leaderboard.csv')
df_lb_pub = df_pub.groupby('user_name').min()
df_lb_pub['last'] = df_pub.groupby('user_name').max()['date']
df_lb_pub = df_lb_pub.drop(['date'], axis=1)
df_lb_pub['entries'] = df_pub.groupby('user_name').count()['score']
df_lb_pub = df_lb_pub.sort_values(['score', 'last'], ascending=True)
df_lb_pub['rank'] = [i for i in range(1, len(df_lb_pub)+1)]
df_lb_pub = df_lb_pub.set_index('rank')
# df_lb_pub = df_lb_pub.reindex(columns=['rank', 'user_name', 'score', 'last', 'entries'])
print(df_lb_pub)

# # %%

# %%
