# Replace with forward value
import pandas as pd
var = pd.read_csv("students.csv")
print(var.replace(20,method="ffill"))