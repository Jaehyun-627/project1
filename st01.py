import streamlit as st
import pandas as pd
import numpy as np

st.title("Product Review Data")

DATA_URL = 'sales_data.csv'
def load_data():
  data = pd.read_csv(DATA_URL)
  return data

data = load_data()
if st.checkbox("Show raw data"):
  st.subheader("Raw Data")
  st.write(data)

agg_data = data.groupbㅛ(["Product"]).mean().reset_index()
st.bar_chart(agg_data, x = "Product", y = "Review Score")
