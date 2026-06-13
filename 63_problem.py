# Drop all Nan value Rows Using->> thresh=3
# thresh stands for minimum number of non-NaN values required to keep a row (or column).
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
var1 = var.dropna(thresh=3)
print(var1)