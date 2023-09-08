import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

points=reviews.loc[(reviews.points>=95)&(reviews.points<=100)]
top_oceania_wines = points.loc[points.country.isin(["Australia","New Zealand"])]

print(top_oceania_wines)