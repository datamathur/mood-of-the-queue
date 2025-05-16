# Mood of the Queue
A tool to help log the mood of the ticket queue throughout the day, and visualize the emotional trend.

### Deliverables
- ***[Hosted App](https://mood-of-the-queue-um.streamlit.app/)***
- ***[GitHub Repo](https://github.com/datamathur/mood-of-the-queue)***
- ***[Google Sheets](https://docs.google.com/spreadsheets/d/1bLnA-wFF987cenKfLPaCXHL6BK-fVd7Iht_Nypc-ATM/edit?usp=drive_link)***
- ***[README File](https://github.com/datamathur/mood-of-the-queue/blob/main/README.md)***

## Features
1. Logs the mood of users:
   1. Select mood from dropdown of **7 moods** (*😐 Neutral, 😊 Happy, 😄 Excited, 😴 Tired, 😰 Stressed, 😠 Angry, 😞 Sad*)
   2. Add an optional note to describe the mood in detail.
2. Add the mood log (*datestamp, timestamp, mood, and note*) to the google spreadsheet database.
3. Mood chart (bar plot) based on date groups (*today, last week, last month, or last year*) which is set on today by default.
4. Auto-updates the chart after each submission.

## Tech-stack
- ***Language***: Python
- ***Frontend/UI***: Streamlit
- ***Storage/Database***: [Google Sheets](https://docs.google.com/spreadsheets/d/1bLnA-wFF987cenKfLPaCXHL6BK-fVd7Iht_Nypc-ATM/edit?usp=drive_link)
- ***Visualization***: Plotly

## Setup Instructions
1. Clone repository
```
git clone https://github.com/datamathur/mood-of-the-queue.git
cd mood-of-the-queue
```
2. Install Requirements
```
pip install -r requirements.txt
```
3. Run the App
```
streamlit run mood_app.py
```

## Thought Process

### Approach
Given the time constraint, I divided the assignment into 3 sections:
1. Design the code with basic functionalities using Python, Streamlit, and Plotly.
2. Create the google spreadsheet and connect it with the python script.
3. Prepare the deliverables:
   1. Test the raw code.
   2. Organize the raw code.
   3. Write the readme file.
   4. Deploy the app on streamlit cloud.

### Potential Next Steps
1. Allow users to add multiple emotions in a single entry.
2. Create a user login system to allow each user to view personal logs (to study their emotional trends) along with the public logs (to view the general mood).
3. Connect the app to a SQL database to allow developers and analysts to perform complex operations.


## About the Author
I am **Utkarsh Mathur**, **Data Scientist at Atriano** with over **2 years of experience** in Data Scientist and Machine Learning Engineer roles. 

I graduated from ***University at Buffalo*** with an ***MS in Data Science*** in June 2024 and I hold a ***B.Tech. from IIT Roorkee***. I am fluent at programming in *Python*, *SQL*, & *R* and I am experienced in ***Front-end and Backend development***, training ***Machine Learning*** and ***Deep Learning*** models, performing ***Data Analytics***, developing ***CI/CD pipelines***, establishing ***ETL/ELT pipelines***, and creating ***Data Visualizations***.

Before starting graduate studies, I was a Data Scientist at Quinbay in Bangalore following internships at Hono and ImagoAI. During my undergraduate education, I worked on research projects in the Departments of Physics and Mathematics at IIT Roorkee.

[Linked](https://www.linkedin.com/in/utkarshmathur1024/) | [Website](https://datamathur.github.io/) | [Email](mailto:utkarsh.mathur@gmail.com)