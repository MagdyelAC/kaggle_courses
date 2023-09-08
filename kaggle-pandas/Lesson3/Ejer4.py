import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

centered_price = reviews.price -reviews.price.mean()
print(centered_price)