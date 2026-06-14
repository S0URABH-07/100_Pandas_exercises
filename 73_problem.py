# Replace all alphabetic letter with perticular value 
import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.replace("[A-Za-z]","python" , regex=True))