# empty list
countries = []
print(countries)

# creating a list with mixed data types
countries = ["Kenya", "Uganda", "Tanzania", "Ethiopia", 254, 256, 255, 252]
print(countries)

# nested
countries = ["Kenya", [254], "Uganda", [256], "Tanzania", [255], "Ethiopia", [251]]
print(countries)

# Access List Elements
print(countries[0])
print(countries[-1])

# List slicing in Python
print(countries[0:5])

# Access Nested List Elements
print(countries[0][1])
print(countries[2][1])

#Change List Item
countries[0] = "MamaKenya"
print(countries)

# Appending  in Python
countries.append("Sudan")
print(countries)

# Extending lists
countries.extend([249, "Somalia", 252 ])
print(countries)

# repeating lists
print(countries * 2)

# deleting item in a list
del countries[8:]
print(countries)

