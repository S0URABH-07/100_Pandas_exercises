# Fill the forward value on Nan place 
import pandas as pd
var = pd.read_csv("students.csv")
print(var.fillna(method="ffill"))