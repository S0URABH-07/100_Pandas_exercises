# Convert into ascending order using ascending() fnxn 

import pandas as pd
var = pd.read_csv("students.csv")
print(var.sort_index(axis=0 , ascending=False)) # axis 0 means according to row assending the data