# Drop all Nan value Rows Using->> inplace=True
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
var.dropna(inplace=True)
print(var)