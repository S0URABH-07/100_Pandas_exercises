# Drop Nan data row using dropna()
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.dropna())