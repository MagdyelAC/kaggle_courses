import pandas as pd
reviews = pd.read_csv("../winemag-data-130k-v2.csv",index_col=0)

renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})
print(renamed)