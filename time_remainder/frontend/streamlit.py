import streamlit as st
import requests

st.markdown('# Time remainder calculator')
st.markdown('#### Instructions: enter in the 2 fields respectively the day of the week expressed as below and the time in this format -> 15:35')
st.markdown('by castoldie')

days = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednsday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}

day_of_week = st.selectbox(
     'How long before...',
     ("Sunday",
    "Monday",
    "Tuesday",
    "Wednsday",
    "Thursday",
    "Friday",
    "Saturday"))

t = st.time_input('at...')

url = 'http://localhost:8000/calculate'
params = {
    'day_of_week': days[day_of_week], # 0 for Sunday, 1 for Monday, ... 
    'time': str(t)
}

response = requests.get(url, params=params).json()

st.markdown(f'## Time left before {day_of_week}: \n ## {response["wait"]}')





