# Join two dataframes 
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"C":[2,3,4,5,7],"D":[10,14,15,16,11]})
print(var1.join(var2))