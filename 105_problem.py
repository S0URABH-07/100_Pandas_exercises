# perform arithmetic fnxn using pivot_table
import pandas as pd
var = pd.DataFrame({"days":[1,1,1,1,2,2],
                    "st_name":["a","b","b","a","b","a"],
                    "eng":[10,12,14,16,10,18],
                    "maths":[17,12,32,45,76,79]
})
print(var.pivot_table(index="st_name",columns="days",aggfunc="mean",margins="True"))