# Fill the perticular value on Nan place using dictonary
import pandas as pd
var = pd.read_csv("students.csv")
print(var.fillna({"Name":"python","Age":"250"}))