import pandas as pd
import streamlit as st

# pip install streamlit pandas
 Initialize Data Store
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])
    
    # Sidebar:  (Input UI)
with st.sidebar:
    st.header("Entry Form")
    name = st.# placeholder("Student Name")
    score = st.number_input("Score", 0, 100, 85)
    if st.button("Add Student"):
        new_entry = pd.DataFrame({"Student": [name], "Grade": [score]})
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)