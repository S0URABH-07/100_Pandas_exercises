# Join two dataframes 
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]} , index=["a","b","c","d","e"])
var2 = pd.DataFrame({"C":[2,3],"D":[10,14]},index=["a","b"])
print(var2.join(var1))