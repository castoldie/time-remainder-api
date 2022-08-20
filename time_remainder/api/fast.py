from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime

from time_remainder.time_calculator.timencoders import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {"Welcome": True}

@app.get("/calculate")
def predict(day_of_week, time):

    now = datetime.now()
    day_of_week = int(day_of_week)

    if day_of_week > now.weekday():

        delta_day = day_of_week - now.weekday()

    else:

        delta_day = 6 - now.weekday() + day_of_week + 1

    then = datetime(year=now.year,
                    month=now.month,
                    day=now.day+delta_day,
                    hour=int(time[:2]),
                    minute=int(time[-2:]))

    wait_prediction = dhms_from_seconds(date_diff_in_seconds(then, now))
    # compute `wait_prediction` from `day_of_week` and `time`
    return {f'wait': "%d days, %d hours, %d minutes, %d seconds" %wait_prediction}