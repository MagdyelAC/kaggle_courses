import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

star_ratings = reviews.points.apply(lambda points: 3 if points >= 95 else (2 if points >= 85 else 1))
star_ratings = pd.Series(star_ratings, name='Stars')