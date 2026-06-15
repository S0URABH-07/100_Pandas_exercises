# Get perticular data using get_group("")
import pandas as pd

var = pd.DataFrame({
    "Name": ["Riya", "John", "Neha", "Arjun", "Sneha"],
    "Marks": [80, 90, 70, 80, 70]
})

var1 = var.groupby("Marks")

for x, y in var1:
    print("Group:", x)
    print(y)
    print()

# Get only the group where Marks = 80
print(var1.get_group(80))