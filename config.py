HIDE_STREAMLIT_STYLE = """
    <style>
        div[data-testid="stToolbar"] {visibility: hidden; height: 0%; position: fixed;}
        div[data-testid="stDecoration"] {visibility: hidden; height: 0%; position: fixed;}
        div[data-testid="stStatusWidget"] {visibility: hidden; height: 0%; position: fixed;}
        #MainMenu {visibility: hidden; height: 0%;}
        header {visibility: hidden; height: 0%;}
        footer {visibility: hidden;height: 0%;}
    </style>
    """

SHEET_NAME = "Mood App (Mochi Take Home Assignment)"

GROUPS = ["Today", "Last Week", "Last Month", "Last Year"]
GROUP_DAYS = {
    "Today": 0, 
    "Last Week": 7, 
    "Last Month": 30, 
    "Last Year": 365
}

CURRENT_MOOD_PLACEHOLDER = "How are you feeling?"
NOTE_PLACEHOLDER = "Would you like to share more about your feeling? (Optional)"

MOODS = {
    "😐 Neutral": "Neutral", 
    "😊 Happy": "Happy", 
    "😄 Excited": "Excited",
    "😴 Tired": "Tired",
    "😰 Stressed": "Stressed",
    "😠 Angry": "Angry",
    "😞 Sad": "Sad"
    }