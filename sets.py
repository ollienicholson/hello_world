# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# Sets cannot have two items with the same value.

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
print(len(thisset))
print(type(thisset))
print(list(thisset))
# print(dict(thisset)) # Error: K-V pair is required
print(str(thisset))
print(tuple(thisset))