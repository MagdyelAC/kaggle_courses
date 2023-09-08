import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine)