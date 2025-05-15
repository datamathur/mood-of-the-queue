import pandas as pd
from config import *
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta
import streamlit as st
from streamlit_gsheets import GSheetsConnection

def return_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn

def get_worksheet():
    # skey = st.secrets["gsheets"]
    # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # creds = Credentials.from_service_account_info(skey, scopes=scope)
    # client = gspread.authorize(creds)
    # sheet = client.open_by_url(SHEET_NAME).sheet1
    conn = return_connection()
    df = conn.read()
    return df

def mood_logger(current_mood, note, df):
    datestamp = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H:%M:%s")
    conn = return_connection()
    df.loc[len(df)] = [datestamp, timestamp, MOODS[current_mood], note]
    conn.update(worksheet='Sheet1', data=df)

def grouping_tool(group, df):
    today = datetime.strftime(datetime.now().date(), "%Y-%m-%d")
    start_date, end_date = datetime.strptime(today, "%Y-%m-%d"), datetime.strptime(today, "%Y-%m-%d")
    if group=="Last Week":
        start_date = datetime.strftime((end_date - timedelta(days=7)).date(), "%Y-%m-%d")
    elif group=="Last Month":
        start_date = datetime.strftime((end_date - timedelta(days=30)).date(), "%Y-%m-%d")
    elif group=="Last Year":
        start_date = datetime.strftime((end_date - timedelta(days=365)).date(), "%Y-%m-%d")
    else:
        start_date = end_date
    df_group = df[(df['Datestamp'] >= start_date) & (df["Datestamp"] <= end_date)]
    return df_group

def graph_tools(df_today):
    mood_counts = df_today['Mood'].value_counts().reset_index()
    mood_counts.columns = ['mood', 'count']
    mood_counts['mood'] = pd.Categorical(mood_counts['mood'], categories=list(MOODS.values()), ordered=True)
    mood_counts = mood_counts.set_index('mood').reindex(list(MOODS.values()), fill_value=0).reset_index()
    return mood_counts