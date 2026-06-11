# fetch last 5 data rows using-> tail() fnxn 
import pandas as pd
fetch_last_rows = pd.read_csv("students.csv")
print(fetch_last_rows.tail())