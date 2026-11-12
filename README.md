# Spotify Genre Dashboard (Mini-Project 2 prototype)

Interactive dashboard comparing six Spotify genres: reggae, dancehall, reggaeton, afrobeat, pop and R&B.

## Research questions

1. Which genre has the highest average popularity? (bar chart)
2. Are longer songs less popular? (scatter plot)
3. What does the spread of tempo look like in each genre? (box plot)

## How to use it

- **Click a bar** to show only that genre in the scatter plot and box plot. Click it again to clear the filter.
- **Drag a box** (or use the lasso tool) on the scatter plot to select songs. The bar chart and box plot recompute for just those songs. Double-click the scatter to clear.
- **Hover** any bar, dot or box for details.
- **Reset filters** clears everything.

## Run it

- Hosted: GitHub Pages (link in the submission).
- Locally: in this folder run `python -m http.server 8000`, then open http://localhost:8000. Double-clicking `index.html` will not load the data because browsers block local file requests.

## Data

- Source: [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset), Kaggle (Maharshi Pandya).
- Cleaning (`prepare_data.py`):
  - kept only the 6 genres (6,000 songs, 1,000 per genre)
  - removed duplicate songs within the same genre (the same track listed as a single and on an album)
  - removed songs with tempo = 0 (no tempo detected)
  - converted duration from milliseconds to minutes
  - result: 4,657 songs
- Columns used: genre, popularity, length (min), tempo (BPM), plus song and artist names for tooltips.

## Encodings

| Data variable | Type | Mark | Channel | Principle |
|---|---|---|---|---|
| Popularity | Quantitative | Bar, point | Y-position | Effectiveness |
| Genre | Categorical | Bar, point, box | X-position + color hue (Okabe-Ito colorblind-safe palette) | Expressiveness |
| Song length | Quantitative | Point | X-position | Effectiveness |
| Tempo | Quantitative | Box | Y-position | Effectiveness |


## Tools

Plotly.js 2.35.2 and PapaParse 5.4.1, loaded from jsDelivr.

Also got help from claude developing interactive dashboard.
