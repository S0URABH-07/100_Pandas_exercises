# How to merge two Dataframes
#merge() is used to combine two DataFrames based on a common column
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[3,4,5,6,7],"C":[10,14,15,16,11]})
print(pd.merge(var1,var2))