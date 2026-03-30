import pandas as pd
import streamlit as st

# Handle the main interface

st.header("Faculty Grade Dashboard")

# Updates the dashboard on the main page
def updateDashboard():
    st.metric("Average", 0)
    st.metric("Highest", 0)
    st.metric("Lowest", 0)

# Handle the UI Sidebar

sd_bar = st.sidebar
sd_bar.header("Entry Form")

## Request for the student name

student_name = sd_bar.text_input("Student Name", placeholder = "Lorem Ipsum")

## Request for their grade

student_grade = sd_bar.number_input("Score", step = 1)

## Add the student to the list

if sd_bar.button("Add Student"):
    ## placeholder
    st.text(f"Added Student {student_name}")
    updateDashboard()