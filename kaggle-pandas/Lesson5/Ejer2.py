import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv")

point_strings = reviews.points.astype('str')
print(point_strings)