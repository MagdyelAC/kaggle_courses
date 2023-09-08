import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

n_missing_prices = reviews.price.isnull().sum()
print(n_missing_prices)