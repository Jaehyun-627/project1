import streamlit as st

import pandas as pd
import numpy as np

from viz2 import DATE_COLUMN

st.title('Simple Sales Data Dashboard')

DATE_COLUMN = 'Product'

def load_data(nrows):
  data = pd.read_csv("sales_data.csv", nrows = nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data
