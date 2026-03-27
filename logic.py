import pandas as pd
import streamlit as st

avg = 0
min = 0
max = 0

# Gives the average, highest, and lowest
def calculate_stats(df):
    """Calculates summary statistics from the grade dataframe."""
    if df.empty:
        return 0, 0, 0
    avg = df["Grade"].mean()
    high = df["Grade"].max()
    low = df["Grade"].min()
    return avg, high, low


def: get_grade_distribution(df)
        """Categorizes grades into letter brackets for plotting."""
    if df.empty:
        return pd.Series(dtype=int)
    bins = [0, 60, 70, 80, 90]
    labels = ['F', 'D', 'C', 'B', 'A']
    return pd.cut(df['Grade'], bins=bins, labels=# placeholder).value_counts().sort_index()