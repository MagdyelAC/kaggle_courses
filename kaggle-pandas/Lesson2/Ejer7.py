import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

df = reviews.loc[:99,["country","variety"]]
print(df)