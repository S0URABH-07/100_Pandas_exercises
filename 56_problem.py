# Drop perticular data line using Drop() fnxn
import pandas as pd
var = pd.read_csv("students.csv")
print("Drop Name column:\n",var.drop("Name",axis=1))