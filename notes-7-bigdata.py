# connor
# today 
# some data notes because "bigdata" is broad

import pandas as pd

# load csv

data = pd.read_csv("Spotify2024.csv")

# preview data

print(data.head())
print(data.column())
print(data.shape())

# columns

print(data["artist"]head())
print(data["track"]head())

# filtering data

popular = data[data["streams"] > x ]
print(popular.head())

# sorting

top_tracks = data.sort_values("streams", ascending = False)
print(top_tracks.head())

# value / frequency

print(data["artist"].value_counts().head())

# basic stats

print(data["streams"].mean()) # avg streams
print(data["streams"].max()) # max
print(data["streams"].min()) # min

# select column

subset = data[["artist", "track", "streams"]]
print(subset.head)

# filtered data

popular.to_csv("popular_songs.csv",index=False)

