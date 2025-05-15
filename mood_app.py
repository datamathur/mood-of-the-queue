# Libraries and Competencies
import streamlit as st
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from config import *
from utils import *
import plotly.express as px
import time

# Page Header
st.set_page_config(page_title="Mood App", page_icon="🧪")

# Importing Google Sheet
sheet = get_worksheet()

# Page Title
st.markdown("<h2 style='text-align: center; padding-bottom: 0em'>Mood of the Queue</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; padding-top: 0.2em; padding-bottom: 2em'>😐😰😊😐😴😞😄</h2>", unsafe_allow_html=True)

# Mood Logging Form
st.markdown("<h3>Log Your Mood 📝</h3>", unsafe_allow_html=True)

## User Entry
current_mood = st.selectbox("✨ Select a mood *", list(MOODS.keys()), index=None, placeholder=CURRENT_MOOD_PLACEHOLDER, key='mood_dropdown') # Dropdown
note = st.text_input("📜 Add a short note", placeholder=NOTE_PLACEHOLDER, key='mood_note') # Optional Note

## Submit Button
st.markdown(
    """
    <style>
    .stButton {
        display: flex;
        justify-content: center;
        padding: "0em,0em,0em,0em";
    }
    </style>
    """,
    unsafe_allow_html=True
)
if st.button("Submit"):
    if current_mood==None:
        st.error("Choose a mood")
    else:
        mood_logger(current_mood, note, sheet)
        st.success("Mood logged successfully!")
        time.sleep(2)
        st.session_state.clear()
        st.cache_data.clear()
        st.rerun()

# Page Divider
st.markdown(
    """
    <hr style="margin-top: 1em; margin-bottom: 1.5em; border-color: #000144; border-width: 2px">
    """,
    unsafe_allow_html=True
)

# Mood Chart
st.markdown("<h3>Mood Chart 📊</h3>", unsafe_allow_html=True)

## Read data from google sheet
df = get_worksheet()
df["Datestamp"] = pd.to_datetime(df["Datestamp"])

## Radio button for date group
group = st.radio(label = "📅 Select date group", options=GROUPS, horizontal=True)
df_group = grouping_tool(group, df)

if not df_group.empty:
    ## Display graph
    mood_counts = graph_tools(df_group) # Prepare data for graph
    fig = px.bar(mood_counts, x='mood', y='count', color='count',
                 title=f"Mood Frequency for {group}", text='count', 
                 color_continuous_scale=px.colors.sequential.RdBu) 
    fig.update_layout(xaxis_title='Mood', yaxis_title='Count')
    st.plotly_chart(fig, use_container_width=True) # Display graph
else:
    ## Display error message
    st.info("No moods logged for today yet.")

# Footer
st.markdown(
    """
    <hr style="margin-top: 0em; margin-bottom: 0.9em; border-color: #000144; border-width: 0.5px">
    <div style="text-align: center; font-size: 0.9em; color: #000144">
        Made with 🪄 by <a href="https://www.linkedin.com/in/utkarshmathur1024/" style="color: #000144"><strong>Utkarsh Mathur</strong></a> ✨
    </div>
    """,
    unsafe_allow_html=True
)

## Remove padding
st.markdown("""
    <style>
        .block-container {padding-bottom: 1rem;}
        .main {padding-bottom: 0px;}
    </style>
    """, 
    unsafe_allow_html=True
)