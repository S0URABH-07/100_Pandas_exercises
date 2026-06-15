# Reshape the dataframes USE-> melt fnxn
import pandas as pd
var = pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[10,12,14,16,10,18],"maths":[17,12,32,45,76,79]})
print(pd.melt(var))