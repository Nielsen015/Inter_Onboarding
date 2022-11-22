# Mophat K 
# @villager

################################################ Tuple ##########################################################
# A tuple is a collection of objects which ordered and immutable. 
# Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike 
# lists and tuples use parentheses, whereas lists use square brackets.

# Create a tuple
interns = ("said", "george", "moses", "maureen", "mophat")
facilitators = ("Beth", "Mkuu")
departments = "DESG", "CQ", "QA", "T24"

# Allows different data types
building_info = ("One Padmore Building", +254202008603)

# Accessing tuples
# Indexing begins at 0
phone_no = building_info[1]
jkuat_alumni = interns[2:4]
current_session = departments[2]

print(phone_no)
print(jkuat_alumni)


################################################ Sets #################################################################
# Mathematically a set is a collection of items not in any particular order. 
# The sets in python are typically used for mathematical operations like union, intersection, difference and complement etc. 
# Python’s built-in set type has the following characteristics:
### Sets are unordered.
### Set elements are unique. Duplicate elements are not allowed.
### A set itself may be modified, but the elements contained in the set must be of an immutable type.

# Create a set
myset = {0, 1, 2, 3, 4}
myset1 = ([5, 6, 7, 8, 9])

# Add item to set
myset = {0, 1, 2, 3, 4}
myset.add("5") # Output 0, 1, 2, 3, 4, 5

# Add sets
myset.update(myset1) # Output 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Access a set
for number in myset:
   print(number) # Output 0, 1, 2, 3, 4

# Nested for loop. Output number in every instance of num
for number in myset:
    for num in myset1:
        print(number) # 0, 0, 1, 1, 2, 2, 3, 3, 4, 4

# Remove item from set
myset = {0, 1, 2, 3, 4}
myset.remove(4) # Output 0, 1, 2, 3

# Set operations
### Set Union
# The union operation on two sets produces a new set containing all the distinct elements from both the sets.
half1 = set(["Jan","Feb","Mar", "Apr", "May", "Jun"])
half2 = set(["Jul","Aug","Sep","Oct","Nov", "Dec"])
FullYear = half1|half2
print(FullYear)

### Set Intersection
# The intersection operation on two sets produces a new set containing only the common elements from both the sets. 
half1 = set(["Jan","Feb","Mar", "Apr", "May", "Jun"])
half2 = set(["Jun", "Jul","Aug","Sep","Oct","Nov", "Dec"])
month_intersect = half1 & half2
print(month_intersect)

### Set Difference
# The difference operation on two sets produces a new set containing only the elements from the first set and none from the second set.
half1 = set(["Jan","Feb","Mar", "Apr", "May", "Jun"])
half2 = set(["Jun", "Jul","Aug","Sep","Oct","Nov", "Dec"])
month_difference = half1 - half2
month_difference1 = half2 - half1
print(month_difference)
print(month_difference1)

### Set Comparison
## We can check if a given set is a subset or superset of another set.
## The result is True or False depending on the elements present in the sets.
half1 = set(["Jan","Feb","Mar", "Apr", "May", "Jun"])
half2 = set(["Jun", "Jul","Aug","Sep","Oct","Nov", "Dec"])
SubsetRes = half1 <= half2
SupersetRes = half2 >= half1
print(SubsetRes)
print(SupersetRes)

