import pandas as pd
from pathlib import Path

# loading clean data
df = pd.read_csv('data/clean/events.csv')
# adding date column
df['date'] = df['timestamp'].str[:10]
# writing transformed data
Path("data/transformed").mkdir(parents=True, exist_ok=True)
df.to_csv('data/transformed/events.csv')