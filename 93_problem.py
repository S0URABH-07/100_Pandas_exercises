# It is used to group rows that have the same value and then perform calculations on each group.
import pandas as pd
var = pd.DataFrame({
    "Name": ["Riya", "John", "Neha", "Arjun", "Sneha"],
    "Marks": [80, 90, 70, 80, 70]
})
var1 = var.groupby("Marks")
for x,y in var1:
    print(x)
    print(y)
    print( )