"""Module providing a function printing python version."""
import os
import pandas as pd
from data_collection import fetch_all
import asyncio


YOUTUBE_API_KEY = 'AIzaSyDDKKNgq__t6jeJE5jTdsFh5vFBOZ6PQrI'

os.environ['YOUTUBE_API_KEY'] = YOUTUBE_API_KEY
def print_python_version():
    print(pd.__version__)

print_python_version()

timeStart = pd.Timestamp.now()

df = pd.read_csv('s3://full-stack-bigdata-datasets/Big_Data/youtube_playlog.csv')

timeEnd = pd.Timestamp.now()

print(f'Time to read the file: {timeEnd - timeStart}')

print(df.head())


song_ids = df['song'].unique().tolist()



required_api_calls = len(song_ids) // 50
time_in_seconds = required_api_calls * 2
time_in_hours = time_in_seconds / 3600
print(f'We need to do {required_api_calls} API calls to fetch all the data.')
print(f'It would take about {time_in_hours:.1f} hours to complete.')

songs_sample = song_ids[:50000]

loop = asyncio.get_event_loop()

task = loop.create_task(fetch_all(songs_sample, dry_run=False))
