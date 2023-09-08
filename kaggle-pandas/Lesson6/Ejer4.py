import pandas as pd

powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

powerlifting_combined = powerlifting_meets.join(powerlifting_competitors, lsuffix='_meets', rsuffix='_competitors')
print(powerlifting_combined)