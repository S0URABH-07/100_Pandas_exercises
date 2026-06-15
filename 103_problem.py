# pivot() changes a long (vertical) table into a wide (horizontal) table.
import pandas as pd
var = pd.DataFrame({"days":[1,2,3,4,5,6],
                    "st_name":["a","b","c","a","b","c"],
                    "eng":[10,12,14,16,10,18],
                    "maths":[17,12,32,45,76,79]
})
print(var.pivot(index="days",columns="st_name"))