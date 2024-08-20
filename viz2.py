import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Sales Data Dashboard')

filename = "sales_data.csv"

def load_data():
  data = pd.read_csv(filename)
  return data

if st.checkbox('Show Raw data'):
  st.subheader('Raw Data')
  st.wrtie(data)

agg_data = data.groupby(['Region']).sum

st.write(agg_data)

# df = pd.DataFrame({'Product'['Product A', 'ProductA', 'ProductA', 'ProductA', 'ProductB', 'ProductB','ProductB','ProductB'], 
#                    'Region'['North', 'South', 'East', 'West','North', 'South', 'East', 'West'],
#                    'Sales'['150', '200', '250', '175', '300', '230', '210', '190']})

