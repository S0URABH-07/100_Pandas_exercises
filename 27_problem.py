# Delete column other method
import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4,5] , "B":[0,9,8,7,6], "C":[5,4,3,2,7]})
print(var)
var.pop("B")
print(var)
