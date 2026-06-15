# concat two Dataframes with axis and join=
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[2,3],"B":[10,14]})
print(pd.concat([var1,var2],axis=1,join="inner"))