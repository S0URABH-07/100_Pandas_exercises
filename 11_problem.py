# Create table using Dictonary
import pandas as pd 
dic = {"name":['python','c','c++','java'] , "Rank":[1,4,3,2]}
var = pd.Series(dic)
print(var)
# if you used mixed type data than the series type is object