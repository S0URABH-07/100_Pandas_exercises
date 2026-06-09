# Dataframes using dictonary
import pandas as pd
dic = {"a":[1,2,3,4,5] , "b":[0,9,8,7,6]}
D = pd.DataFrame(dic)
print(D)
print(type(D))