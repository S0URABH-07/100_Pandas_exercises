# Change data in your csv file

import pandas as pd
var = pd.read_csv("students.csv")
var.loc[0,"Name"] = "Python"
print(var)