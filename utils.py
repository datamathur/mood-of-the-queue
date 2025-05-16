import pandas as pd
from config import *
from datetime import datetime, timedelta, timezone
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px
import time

# Create and return connection with spreadsheet.
def return_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn

# Fetch data from and spreadsheet and return dataframe
def get_worksheet():
    conn = return_connection()
    df = conn.read()
    return df

# Logs user mood to spreadsheet
def mood_logger(current_mood, note, df):
    ## Create mood log
    now = datetime.now(timezone.utc)
    datestamp = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%H:%M:%S")
    df.loc[len(df)] = [datestamp, timestamp, MOODS[current_mood], note]
    
    ## Append log to spreadsheat
    conn = return_connection()
    conn.update(worksheet='Sheet1', data=df)

# Create graph based on user input for mood visualization
@st.fragment
def graph_tools(group):
    ## Fetch data from spreadsheet
    df = get_worksheet()
    df["Datestamp"] = pd.to_datetime(df["Datestamp"])

    ## Group data based on user input
    now = datetime.now(timezone.utc)
    today = datetime.strftime(now, "%Y-%m-%d")
    end_date = datetime.strptime(today, "%Y-%m-%d")
    start_date = datetime.strftime((end_date - timedelta(days=GROUP_DAYS[group])).date(), "%Y-%m-%d")
    df_group = df[(df['Datestamp'] >= start_date) & (df["Datestamp"] <= end_date)]

    ## Display graph if values available
    if not df_group.empty:
        ### Aggregate values for bar graph
        mood_counts = df_group['Mood'].value_counts().reset_index()
        mood_counts.columns = ['mood', 'count']
        mood_counts['mood'] = pd.Categorical(mood_counts['mood'], categories=list(MOODS.values()), ordered=True)
        mood_counts = mood_counts.set_index('mood').reindex(list(MOODS.values()), fill_value=0).reset_index()

        ### Create Garph
        fig = px.bar(mood_counts, x='mood', y='count', color='count',
                    title=f"Mood Frequency for {group}", text='count', 
                    color_continuous_scale=px.colors.sequential.RdBu) 
        fig.update_layout(xaxis_title='Mood', yaxis_title='Count')
        st.plotly_chart(fig, use_container_width=True)

        ### Auto-refresh after 1 minute
        st.info(f"Last Refreshed {datetime.strftime(now, '%Y-%m-%d %H:%M:%S')} UTC")
        time.sleep(60)
        st.session_state.clear()
        st.cache_data.clear()
        st.rerun()
    
    ## Display error message if values unavailable
    else:
        st.info("No moods logged for today yet.")
        time.sleep(60)
        st.rerun()