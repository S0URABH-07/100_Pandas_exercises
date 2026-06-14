# Replace using dictonary 
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.replace({"Name":'[A-Z]'},22,regex=True))