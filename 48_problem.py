# fetch perticular rows using slicing
import pandas as pd
fetch_last_rows = pd.read_csv("students.csv")
print(fetch_last_rows[3:6])