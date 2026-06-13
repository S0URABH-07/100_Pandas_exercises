# Fill the perticular value on Nan place
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.fillna("python"))