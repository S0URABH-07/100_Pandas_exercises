# fetch perticular value use-> iloc[]
import pandas as pd
var = pd.read_csv("students.csv")
print(var.iloc[0,2])