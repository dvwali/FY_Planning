import streamlit as st
import pandas as pd
#from st_aggrid import AgGrid

def load_data():
    data = pd.read_csv('FY_Planning/Page1_SW.csv')
    return data

st.title("ST app with data from GH")

try:
    data = load_data()
    st.write("Data loaded")
except Exception as e:
    st.write("Error:", e)
    data = pd.DataFrame()

if not data.empty:
    AgGrid(data)
else:
    st.write("No data")
