# insert columns
import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4,5] , "B":[0,9,8,7,6]})
print(var)
var.insert(2,"Insert",var["A"])
print(var)