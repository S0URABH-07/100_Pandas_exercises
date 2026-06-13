# Replace all Nan value with perticular value ->> inplace=True
import pandas as pd
var = pd.read_csv("students.csv")
var.fillna(15, inplace=True)
print(var)