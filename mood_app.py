# Libraries and Competencies
import streamlit as st
from config import *
from utils import *
import time

# Page Header
st.set_page_config(page_title="Mood App", page_icon="🧪")
st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)

# Page Title
st.markdown("<h2 style='text-align: center; padding-bottom: 0em'>Mood of the Queue</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; padding-top: 0.2em; padding-bottom: 2em'>😐😰😊😐😴😞😄</h2>", unsafe_allow_html=True)

# Mood Logging Form
st.markdown("<h3>Log Your Mood 📝</h3>", unsafe_allow_html=True)

## User Entry
st.markdown("✨ Select a mood *")
current_mood = st.selectbox(CURRENT_MOOD_PLACEHOLDER, list(MOODS.keys()), index=None, key='dropdown') # Dropdown
st.markdown("")
st.markdown("📜 Add a short note")
note = st.text_input(NOTE_PLACEHOLDER, key='note') # Optional Note

## Submit Button
st.markdown(
    """
    <style>
        .stButton {display: flex; justify-content: center; padding: "0em,0em,0em,0em";}
    </style>
    """,
    unsafe_allow_html=True
)
if st.button("Submit"):
    if current_mood==None:
        st.error("Choose a mood")
    else:
        sheet = get_worksheet()
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

## Radio button for date group
group = st.radio(label = "📅 Select date group", options=GROUPS, horizontal=True)
graph_tools(group)

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