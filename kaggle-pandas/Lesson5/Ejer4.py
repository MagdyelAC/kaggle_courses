import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

rev=reviews.region_1.fillna("Unknown")
reviews_per_region = rev.value_counts().sort_values(ascending=False)
print(reviews_per_region)