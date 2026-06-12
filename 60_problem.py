# Drop Nan rows--> Remove nan data row using how="any" to drop rows
import pandas as pd
var = pd.read_csv("Test.csv")
print(var)
print(var.dropna(how="any"))