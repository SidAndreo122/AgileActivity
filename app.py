import pandas as pd
import streamlit as st

# Main variables

df = None
testing = True

# Handle the main interface

st.header("Faculty Grade Dashboard")

# Load data

## Create the data for the session
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])

# Updates the dashboard on the main page
def updateDashboard():
    data = None

    # Test input data
    if testing:
        data = {
            "avg": 0.4555,
            "high": 89,
            "low": 59
        }

    c1, c2, c3 = st.columns(3)
    c1.metric("Average", data["avg"])
    c2.metric("Highest", data["high"])
    c3.metric("Lowest", data["low"])

    st.subheader("Grade Distribution")
    st.bar_chart(df)

    st.subheader("Current Roster")
    st.table(df)

# Adds the student to the data entries (updates the dashboard)
def addStudent(student_name, score):
    new_entry = pd.DataFrame({"Student": [student_name], "Grade": [score]})
    st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
    #df = st.session_state.data
    updateDashboard()

# Tell the user to begin inputing data
if not st.session_state.data.empty:
    df = st.session_state.data
    updateDashboard()
else:
    st.info("No students inputed.")

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
    ## st.text(f"Added Student {student_name}")
    addStudent(student_name, student_grade)