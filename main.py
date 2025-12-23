import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("spotify_data.csv")
#print(df.head())
#print(df.columns)
#print(df[['track_name','album_name','artist_name','track_duration_min']])

top_artists = df['artist_name'].value_counts()
print(top_artists)

#visualization
top_artists.head(20).plot(kind="pie")
top_artists.head(20).to_csv("top_artists.csv")

