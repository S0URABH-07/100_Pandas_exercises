# Read csv file and fetch all columns name
import pandas as pd
fetch_csv = pd.read_csv("students.csv")
print(fetch_csv)
print(fetch_csv.columns)