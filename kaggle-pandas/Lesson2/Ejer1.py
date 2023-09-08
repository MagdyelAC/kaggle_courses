import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")
desc = reviews.description
print(desc)