# Access perticular data
import pandas as pd
dic = {"a":[1,2,3,4,5] , "b":[0,9,8,7,6] , "c":[1,2,3,4,5], 1:['a','b','c','d','e']}
D = pd.DataFrame(dic)
print(D)
print(type(D))
print(D["b"][2])