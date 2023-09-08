import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

best_rating_per_price = reviews.groupby('price').points.max()
print(best_rating_per_price)