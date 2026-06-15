# Join two dataframes and use suffixes
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]} , index=["a","b","c","d","e"])
var2 = pd.DataFrame({"A":[2,3],"B":[10,14]},index=["a","b"])
print(var2.join(var1,how="outer",rsuffix="_right",lsuffix="_left"))