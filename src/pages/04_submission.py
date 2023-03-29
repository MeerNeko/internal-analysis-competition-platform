import datetime 
import streamlit as st 
import pandas as pd
import pandera as pa
from pandera.typing import Series, DataFrame
from pandera.errors import SchemaError

from eval_metric import rmse

class SubmissionSchema(pa.SchemaModel):
    account_id: Series[str] = pa.Field(nullable=False, unique=True)
    target: Series[float] = pa.Field(nullable=False)

    class Config:
        strict = True

def validate_submission(df:pd.DataFrame) -> DataFrame[SubmissionSchema]:
    st.write(df)
    try:
        df_validated = SubmissionSchema.validate(df)

    except SchemaError as e:
        st.write(e)
        df_validated = None

    sample_submission = pd.read_csv('./asset/sample_submission.csv')
    assert len(df_validated)==len(sample_submission), 'submission.csv must be the same length as sample_submission'
    return df_validated


user_name = st.selectbox(
    'Select user',
    ('ito', 'akimoto', 'akahoshi', 'ohta'))

uploaded_file = st.file_uploader(label="Let's submit submission.csv !", type='csv', accept_multiple_files=False)

if uploaded_file is not None:
    st.write('Upload success!')
    df = pd.read_csv(uploaded_file)
    df_validated = validate_submission(df)

    ground_truth_df = pd.read_csv('./asset/ground_truth.csv')
    rmse_score = rmse(ground_truth_df['target'], df_validated['target'])

    df_lb = pd.read_csv('./asset/leader_board.csv')
    dt_now = datetime.date.today()
    df_lb = df_lb.append({'user_name': user_name, 'score': rmse_score, 'date': dt_now}, ignore_index=True)
    df_lb.to_csv('./asset/leader_board.csv', index=False) 




