import timeit
# ==== PyTricks from Real Python ====

# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango",
]
newlist = []

for item in fruits:
    if "a" in item:
        newlist.append(item)

# print("\n", newlist, "without list comprehension")

# With list comprehension you can do all that with only one line of code:
newlist = [item for item in fruits if "a" in item]

# print("\n", newlist, " >> using list comprehension")
# print("\n", fruits, " >> the old list remains unchanged")

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

# With no if statement:
newlist = [x for x in fruits]
# print(newlist, "no if statements")

# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
# print("\n", newlist, ">> using range")

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
# print("\n", newlist, ">> using Upper")

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
# print("\n", newlist, " >> set all elements as 'hello'")

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
# print("\n", fruits, ">> original list")
# print("", newlist, " >> returns orange instead of banana")

# ===== Python's list comprehensions are awesome =====
collection = 1, 2, 3, 4, 5

vals = [value for value in collection if value != 3]

# print("\n", vals, " >> this is vals")
# print("\n", collection, " >> this is collection")


# This is equivalent to:
def old_list(i):
    vals = []  # list is empty
    for item in i:
        if item != 3:
            vals.append(item)
    return vals  # returns everything but 3


# print(old_list(collection))

# Example:
even_squares = [x * x for x in range(10) if not x % 2]

# print(even_squares, ">> this is even_squares")


# interesting way to assign a function to a variable and then call that function
def _myfunc(a, b):
    return a * b


funcs = _myfunc
# print(funcs)

# print(funcs(2, 3))

# "is" vs "=="
a = [1, 2, 3]
b = a

# print(a is b)  # True
# print(a == b)  # True

c = list(a)
# print(a == c)  # True
# print(a is c)  # False

# • "is" expressions evaluate to True if two
#   variables point to the same object

# • "==" evaluates to True if the objects
#   referred to by the variables are equal

# =========
# The "timeit" module lets you measure the execution
# time of small bits of Python code

timeit.timeit("-".join(str(n) for n in range(100)), number=10000)

print("\n", timeit.timeit())
