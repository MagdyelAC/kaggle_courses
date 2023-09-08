import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

price_extremes = reviews.groupby('variety').price.agg([min,max])
print(price_extremes)