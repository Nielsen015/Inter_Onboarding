##### DICTIONARIES

## Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

#You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value

#For example:

east_africa = {
    "Kenya" : "Nairobi",
    "Tanzania" : "Arusha",
    "Uganda" : "Kampala",
    "Ethiopia" : "Addis Ababa",
    "Rwanda" : "Kigali",
    "Burundi" : "Bujumbura",
    "DRC" : "Kinshasa",
    "South Sudan": "Juba"
}

# The above dictionary maps a city to the name of its corresponding country in east africa

# You can also create a dictionary using the built in dict() function as below:

afrika_mashariki = dict([
    ("Kenya" , "Nairobi"),
    ("Tanzania" , "Arusha"),
    ("Uganda" , "Kampala"),
    ("Ethiopia" , "Addis Ababa"),
    ("Rwanda" , "Kigali"),
    ("Burundi" , "Bujumbura"),
    ("DRC" , "Kinshasa"),
    ("South Sudan", "Juba")
    ])

    #If the key values are simple strings, they can be specified as keyword arguments. So here is yet another way to define the dictionary

nyumbani = dict(
    Kenya = "Nairobi",
    Tanzania = "Arusha",
    Uganda = "Kampala",
    Ethiopia = "Addis Ababa",
    Rwanda = "Kigali",
    Burundi = "Bujumbura",
    DRC = "Kinshasa",
    South_Sudan = "Juba"
)

print (type(east_africa))

print (type(afrika_mashariki))

print (type(nyumbani))


##### Accessing dictinary values

# Dictionary elements are not accessed by numerical index. A value is retrieved from a dictionary by specifying its corresponding key in square brackets as below:

print(east_africa["DRC"])

# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value, as below:

east_africa["Somalia"] = "Mogadishu"

print(east_africa)

# If you want to update an entry, you can just assign a new value to an existing key

east_africa["Somalia"] = "Kismayu"

print(east_africa)


# To delete an entry, use the del statement, specifying the key to delete

del east_africa["Somalia"]

print(east_africa)







# print(east_africa)

# print(afrika_mashariki)

# print(nyumbani)


