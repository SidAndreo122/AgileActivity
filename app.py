import pandas as pd
import streamlit as st
import logic

# Main variables

df = None

# Handle the main interface

st.header("Faculty Grade Dashboard")

# Load data

## Create the data for the session
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])

# Adds the student to the data entries (updates the dashboard)
def addStudent(student_name, score):
    new_entry = pd.DataFrame({"Student": [student_name], "Grade": [score]})
    st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

# Handle the UI Sidebar

sd_bar = st.sidebar
sd_bar.header("Entry Form")

## Request for the student name

student_name = sd_bar.text_input("Student Name", placeholder = "Lorem Ipsum")

## Request for their grade

student_grade = sd_bar.number_input("Score", step = 1)

## Add the student to the list

if sd_bar.button("Add Student"):
    addStudent(student_name, student_grade)

# Tell the user to begin inputing data
if not st.session_state.data.empty:
    df = st.session_state.data

    avg, max, min = logic.calculate_stats(df)
    c1, c2, c3 = st.columns(3)
    c1.metric("Average", f"{avg:.1f}")
    c2.metric("Highest", max)
    c3.metric("Lowest", min)

    st.subheader("Grade Distribution")
    st.bar_chart(logic.get_grade_distribution(df))

    st.subheader("Current Roster")
    st.table(df)
else:
    st.info("No students inputed.")