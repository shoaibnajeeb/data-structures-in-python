# DATA STRUCTURES IN PYTHON
import copy

# LIST
# an ordered collection of objects
# contain different types of elements; list element can be any python object
# Define a list
x = [1, 2, 3]

x = [5, "six", [1, 2, 3]]
# Accessing list elements / List indexing
x1 = ["one", "two", "three", "four"]
x1[0]
x1[1]

x1[-1] # negative indexing
x[-2]

# List slicing
x1[0:2]
x1[2:-1]
x1[:2]

# Modifying the list
x2 = [1, 2, 3, 4, 5, 6, 7, 8]
x2[1] = "two"
x2[2:5] = [66, 77, 88]
x2[:0] = [100, 200, 300]
x2[2:5] = []  # delete list elements

# List methods
x3 = [12, 13, 14]
x3.append(15)

x3.extend([7, 8, 9])

x3.insert(2, 100)

x3.sort()

# List concatenation
x4 = ["a", "b", "c"] + [1, 2]

# index and count methods
x4.index("a")
x4.append("a")
x4.count("a")

# Count the elements in list
len(x4)

# min and max of list elements
min([23, 45, 24, 12, 17, 88])
max([23, 45, 24, 12, 17, 88])

# copy lists
x5 = x4.copy()
x6 = copy.deepcopy(x4)

# TUPLE
# Similar to lists, but are immutable
# can contain different data types
# Define a tuple
t1 = (1, 2, 3)
t1 = (1,)

# indexing works the same as lists but not assigning/modifying

# tuples can be concatenated using + operator
t2 = (1, 2, 3) + (4, 5, 6)

# packing and unpacking
(one, two, three, four) = (1, 2, 3, 4)
one, two, three, four = 1, 2, 3, 4

# Converting to list
list1 = list(t2)

# STRINGS
# sequences of characters
# Define a string
s = "Hello world"
s[0]
s[-1]
s[2:]

len(s)  # gives the length of the string
# strings are not mutable and cannot be modified
# split and join method
s1 = "data,science,with,python"
s11 = s1.split(",")
" ".join(s11)

s2 = "Welcome to day one of the python course"
s2.split()

# case conversions
s12 = s1.upper()
s12.lower()

# convert to number
int("10006")
float("156.89")

# strip, lstrip, rstrip
s3 = "   machine learning      "
s3.strip()
s3.lstrip()
s3.rstrip()

# find, index, startswith, endswith

# Modify strings
s4 = "Are machine learning and pattern recognition the same thing"
s4.replace("and", "&")

# String formatting
"{0} is different from {1} and {2}".format("ML", "AL", "PR")
"Are {ml} and {pr} the same thing".format(pr="pattern recognition", ml="machine learning")


# DICTIONARIES
# Pythons version of hash maps/associative arrays
# Used for representing key:value data
# Define a dictionary
y = {"a": 12}
y["b"] = 15
print(y)

# Basic dictionary methods
y.keys()  # list all keys
y.items()  # list all items
y.values()  # list all values
y.get("b")  # returns the value for key "b"
y.update({"c": 22})  # update the dict with the new item

# len function gives the number of items in a dict

# copy and delete
z = y.copy()   # shallow copy
p = copy.deepcopy()

del(y["c"])  # deletes the item with key "c"





