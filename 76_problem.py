# Replace with backward value
import pandas as pd
var = pd.read_csv("students.csv")
print(var.replace(20,method="bfill"))