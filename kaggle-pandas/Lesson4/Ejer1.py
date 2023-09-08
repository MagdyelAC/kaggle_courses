import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

reviews_written = reviews.groupby('taster_twitter_handle').size()
print(reviews_written)