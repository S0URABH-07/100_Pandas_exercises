# Add two series and make one Dataframes
import pandas as pd
sr = {"s":pd.Series([1,2,3,4,5]),"r":pd.Series([0,9,8,7,6])}
var = pd.DataFrame(sr)
print(var)
print(type(var))