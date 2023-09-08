import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

first_description = reviews.description[0]
print(first_description)