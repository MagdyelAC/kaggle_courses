import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

italian_wines = reviews.loc[reviews.country=="Italy"]
print(italian_wines)