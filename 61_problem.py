# Drop perticular column Nan value USing sebset=["clm name"]
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.dropna(subset=["Name"]))