# fetch starting 5 rows of data using head() fnxn
# use head() and fetch top 5 data rows

import pandas as pd 
fetch_data = pd.read_csv("students.csv")
print(fetch_data.head())