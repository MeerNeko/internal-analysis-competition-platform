import tomllib
import datetime 
import streamlit as st 
import numpy as np
from PIL import Image
import pandas as pd
import pandera as pa
from pandera.typing import Series, DataFrame
from pandera.errors import SchemaError

from src.utils import get_config, read_mdfile
from src.eval_metric import rmse

config = get_config()
HOME_DIR = st.session_state['home_dir']

class SubmissionSchema(pa.SchemaModel):
    row_id: Series[str] = pa.Field(nullable=False, unique=True)
    target: Series[float] = pa.Field(nullable=False)

    class Config:
        strict = True

def validate_submission(df:pd.DataFrame) -> DataFrame[SubmissionSchema]:
    sample_submission = pd.read_csv(HOME_DIR / 'asset/sample_submission.csv')
    assert len(df)==len(sample_submission), 'submission.csv must be the same length as sample_submission'
    try:
        df_validated = SubmissionSchema.validate(df)

    except SchemaError as e:
        st.write(e)
        df_validated = None
    
    return df_validated

def split_public_private(df:pd.DataFrame):
    df['month'] = df['row_id'].apply(lambda x: x[4:6])
    public_set = df[df['month']=='01']
    private_set = df[df['month']=='02']

    return public_set, private_set

header_image = Image.open(HOME_DIR / 'asset/SI_Data_Analysis_Challenge_1_header.png')
st.image(header_image)

users = tuple(config['app']['users'])

user_name = st.selectbox('Select user', users)

uploaded_file = st.file_uploader(label="Let's submit submission.csv !", type='csv', accept_multiple_files=False)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_validated = validate_submission(df)
    st.write('Upload success!')

    df_ground_truth = pd.read_csv(HOME_DIR / 'asset/ground_truth.csv')
    df_result = pd.merge(df_ground_truth, df_validated, on='row_id')
    public_set, private_set = split_public_private(df_result)

    rmse_score_pub = rmse(public_set['ground_truth'], public_set['target'])
    rmse_score_pri = rmse(private_set['ground_truth'], private_set['target'])
    st.write(f'Your Score is {rmse_score_pub:.3f}, Great job!')

    df_lb_pub = pd.read_csv(HOME_DIR / 'asset/public_leaderboard.csv')
    df_lb_pri = pd.read_csv(HOME_DIR / 'asset/private_leaderboard.csv')
    dt_now = datetime.date.today()
    df_lb_pub = df_lb_pub.append({'user_name': user_name, 'score': np.round(rmse_score_pub, decimals=3), 'date': dt_now}, ignore_index=True)
    df_lb_pri = df_lb_pri.append({'user_name': user_name, 'score': np.round(rmse_score_pri, decimals=3), 'date': dt_now}, ignore_index=True)
    df_lb_pub.to_csv(HOME_DIR / 'asset/public_leaderboard.csv', index=False)
    df_lb_pri.to_csv(HOME_DIR / 'asset/private_leaderboard.csv', index=False)




