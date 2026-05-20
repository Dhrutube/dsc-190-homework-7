import pandas as pd
from pathlib import Path

# loading raw data
df = pd.read_csv('data/raw/events.csv')
# dropping rows that have any missing fields
df.dropna(inplace=True)
# dropping rows with invalid event types
valid_event_types = {'click', 'login', 'purchase', 'scroll', 'view'}
df = df[df['event_type'].isin(valid_event_types)]
# dropping rows with non-positive duration_seconds
df = df[df['duration_seconds'] > 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)
# normalizing timestamp to ISO 8601
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=False, format='mixed').dt.strftime('%Y-%m-%dT%H:%M:%SZ')
# writing clean data
Path("data/clean").mkdir(parents=True, exist_ok=True)
df.to_csv('data/clean/events.csv')