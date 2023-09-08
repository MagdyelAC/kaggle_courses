import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

df = reviews.loc[[0,1,10,100],["country", "province", "region_1","region_2"]]

print(df)