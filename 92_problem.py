# concat two Dataframes Diffrent dictonary
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"C":[2,3,4,5,6]})
print(pd.concat([var1,var2]))