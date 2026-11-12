"""
prepare_data.py
Cleans the Kaggle "Spotify Tracks Dataset" (Maharshi Pandya) for the dashboard.

Steps:
  1. Keep only the 6 genres from the proposal.
  2. Keep only the columns the dashboard uses.
  3. Convert duration from milliseconds to minutes.
  4. Drop rows with tempo = 0 (no tempo detected) and rows missing key values.
  5. Drop exact duplicate songs within the same genre
     (the same track can appear as a single and on an album).

Usage:  python prepare_data.py dataset.csv data/spotify_6genres.csv
"""
import sys
import pandas as pd

GENRES = ["reggae", "dancehall", "reggaeton", "afrobeat", "pop", "r-n-b"]
COLUMNS = ["track_name", "artists", "track_genre", "popularity",
           "duration_ms", "tempo", "explicit"]

src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(src)
before = len(df[df.track_genre.isin(GENRES)])

df = df[df.track_genre.isin(GENRES)][COLUMNS]
df = df.dropna()
df = df[df.tempo > 0]
df = df.drop_duplicates(subset=["track_name", "artists", "track_genre"])

df["length_min"] = (df.duration_ms / 60000).round(2)
df["tempo"] = df.tempo.round(1)
df["explicit"] = df.explicit.map({True: "Explicit", False: "Clean"})
df = df.drop(columns=["duration_ms"])

df.to_csv(out, index=False)
print(f"Rows in 6 genres: {before} -> after cleaning: {len(df)}")
print(df.track_genre.value_counts().to_string())
