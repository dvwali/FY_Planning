import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, GridUpdateMode, AgGridReturn, ColumnsAutoSizeMode

from st_aggrid.grid_options_builder import GridOptionsBuilder

from snowflake.snowpark.context import get_active_session

session = get_active_session()

def page1():
    st.title("Software")

    #Region Drop-down
    RegionOption1 = st.selectbox(
        "Select a Region:",
        ["---","NA","CN","EU","JP"]
    )
    if RegionOption1 == "---":
        st.write("")
    else:
        st.write("You chose the ", RegionOption1," region.")

    #Type Drop-down
    #Type1 = st.selectbox(
        #"Select the Type of clients:",
        #["---","N","T"])
    #if Type1 == "---":
        #st.write("")
    #else:
        #st.write("You chose the ", Type1," types of clients")
    
    #Data table from Snowflake table
    sql = f"select * from FY_PLANNING_STREAMLIT.RANDOM.PAGE1_SW"
    data = session.sql(sql).to_pandas()
    if RegionOption1 == "---":
        st.write("")
    else:
        filtereddata = data[data['REGION'] == RegionOption1] #and data[data['TYPE'] == Type1]

    # Submit button using "with" syntax
    with st.form(key='my_form'):
	       submit_button = st.form_submit_button(label='Submit')

def page2():
    st.title("Hardware") 

    #Region Drop-down
    RegionOption2 = st.selectbox(
        "Select a Region",
        ["---","NA","CN","EU","JP"]
    )
    if RegionOption2 == "---":
        st.write("")
    else:
        st.write("You chose the ", RegionOption2," region.")
    
    #Data table from Snowflake table
    sql = f"select * from FY_PLANNING_STREAMLIT.RANDOM.PAGE2_HW"
    data = session.sql(sql).to_pandas()
    if RegionOption2 == "---":
        st.write("")
    else:
        filtereddata = data[data['REGION'] == RegionOption2]
        st.table(filtereddata)

    # Submit button using "with" syntax
    with st.form(key='my_form'):
	       submit_button = st.form_submit_button(label='Submit')

def page3():
    st.title("Intellectual Property")

    #Region Drop-down
    RegionOption3 = st.selectbox(
        "Select a Region",
        ["---","NA","CN","EU","JP"]
    )
    if RegionOption3 == "---":
        st.write("")
    else:
        st.write("You chose the ", RegionOption3," region.")
    
    #Data table from Snowflake table
    sql = f"select * from FY_PLANNING_STREAMLIT.RANDOM.PAGE3_IP"
    data = session.sql(sql).to_pandas()
    if RegionOption3 == "---":
        st.write("")
    else:
        filtereddata = data[data['REGION'] == RegionOption3]
        st.table(filtereddata)
    # Submit button using "with" syntax
    with st.form(key='my_form'):
	       submit_button = st.form_submit_button(label='Submit')

def page4():
    st.title("Practice")

    #Region Drop-down
    RegionOption4 = st.selectbox(
        "Select a Region",
        ["---","NA","CN","EU","JP"]
    )
    
    #Data table from Snowflake table
    sql = f"select * from FY_PLANNING_STREAMLIT.RANDOM.PAGE3_IP"
    data = session.sql(sql).to_pandas()
    filtereddata = data[data['REGION'] == RegionOption4]
    st.table(filtereddata)
    AgGrid(filtereddata)

page_names_to_funcs = {
    "Software": page1,
    "Hardware": page2,
    "Intellectual Property": page3,
    "Practice": page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
