# Fill the Nan value with the forward value
import pandas as pd
var = pd.read_csv("students.csv")
print(var.fillna(method="ffill"))