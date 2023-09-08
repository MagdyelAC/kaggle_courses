import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)