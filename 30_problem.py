# Write csv file without index
import pandas as pd
dic = {1:[1,2,3,4,5,6], 2:[9,8,7,6,5,4] , 3:[11,22,33,44,55,66]}
S = pd.DataFrame(dic)
print(S)
S.to_csv("Test1.csv",index=False)