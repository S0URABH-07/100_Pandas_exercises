# Replace value to other value Using-> replace
import pandas as pd
var = pd.read_csv("students.csv")
print(var.replace(to_replace=20,value=25))