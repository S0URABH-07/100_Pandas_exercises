# Drop Nan data with axis using dropna()
import pandas as pd
var = pd.read_csv("Test.csv")
print(var)
print(var.dropna(axis=1))