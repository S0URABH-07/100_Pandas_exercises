# Replace multiple values with one value 
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.replace([20,21,85],500))