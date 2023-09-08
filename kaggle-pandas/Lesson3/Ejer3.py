import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)