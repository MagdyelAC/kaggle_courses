import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

sample_reviews = reviews.iloc[[1,2,3,5,8]]

sample_reviews