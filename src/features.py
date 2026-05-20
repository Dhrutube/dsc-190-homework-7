import pandas as pd
from pathlib import Path

# loading clean data
df = pd.read_csv('data/transformed/events.csv')
# adding column duration_minutes
df['duration_minutes'] = df['duration_seconds'] // 60
# adding weekday column
df['weekday'] = pd.to_datetime(df['date']).dt.day_name()
# writing transformed data
Path("data/features").mkdir(parents=True, exist_ok=True)
df.to_csv('data/features/events.csv')