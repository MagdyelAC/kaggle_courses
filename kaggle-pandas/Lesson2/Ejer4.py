import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

first_descriptions = reviews.loc[0:9,"description"]

print(first_descriptions)