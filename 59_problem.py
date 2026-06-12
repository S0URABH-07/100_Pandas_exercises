# Drop Nan row--> All row data is Nan using how="all" to drop row
import pandas as pd
var = pd.read_csv("Test.csv")
print(var)
print(var.dropna(how="all"))