import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

country_variety_counts = reviews.groupby(['country','variety']).variety.size().sort_values(ascending=False)
print(country_variety_counts)