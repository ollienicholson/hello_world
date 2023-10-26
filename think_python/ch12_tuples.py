from structshape import structshape

t = 'a', 'b', 'c', 'd', 'e', 'f',  # <class 'tuple'>
t1 = ('a', 'b', 'c', 'd', 'e', 'f')  # <class 'tuple'>
t5 = ('a', 'b', 'c', 'd', 'e', 'f')  # <class 'tuple'>
t2 = 'a',  # <class 'tuple'> if you throw a comma at the end
numbers = 1, 2, 3, 4, 5, 6

t3 = 'a'  # this is actually <class 'string'> !!
t4 = ('a')  # this is actually <class 'string'> !!

tup = tuple('blah')  # built-in tuple function
# returns ('b', 'l', 'a', 'h')

# t = (('A', ) + t[1:])
# this function makes a new tuple and makes t refer to it, replacing 'a' with 'A'
(0, 1, 2) < (0, 3, 4)
# returns True

(0, 1, 2000) < (0, 3, 4)
# travereses though the elements until it finds two elements that differ i.e 2000 < 4, still returns True as these subsequent numbers are not considered.. weird right?

a, b = 1, 2
# a = 1, b = 2

a, b = 'b', 'a'
# a = 'b', b = 'a'

addr = 'ollie.nicholson@gmail.com'
name, domain = addr.split('@')  # returns ollie.nicholson, gmail.com

# print(
#     divmod(7, 3), ">> divmod example 1"
# )  # divides 7 by 3, returns results, then returns remainder i.e (7/3 = 2, remainder = 1)

# the following function is a  better way of print divmod, as it saves the quotient to "quot", and saves the remainder to "rem"
quot, rem = divmod(7, 3)  #---> runs in terminal, not in VSCode

# print(quot, rem, "quot & rem")


def min_max(t: tuple) -> tuple:
    return min(t), max(t)


# print(min_max(numbers))


# "*args" gathers all arguments into a tuple
def printall(*args):
    print(*args)


# print(printall(1, 2.0, '3'), "*args unpacks all")

# using '*' we 'scatter' the tuple in order to pass it into divmod
a = 7, 3

# print(divmod(*a))


# sumall takes any number of arguments and returns their sum
def sumall(*args):
    return sum(*args)


# print(sumall(a))

# "zip" combines two or more sequences a returns a list of tuples (kinda like a dict), where each tuple contains one element from each sequence.
# the resutling key-value pairs are easily accessed via a 'for' loop
# the for loop will only execute elements which correspond to one another. If one sequence is longer than the other, the additional elements will not be accessed.

# print(zip(t, numbers), "zip ex1")

# for pair in zip(t, numbers):
#     print(pair)

# print(zip('abcdef', range(3), range(4)), "zip ex2")

# for kvp in zip('abcdef', range(3), range(4)):
#     print(kvp)

# print(list(zip(t, numbers)), "zip the list")

z = list(zip(t, numbers))

# unpack elements with a for loop
# for letter, number in z:
#     print(letter, number)


def has_match(tup1, tup2):
    for x, y in zip(tup1, tup2):
        if x == y:
            return True
        return False


# print(has_match(t1, t))

#  traverse through elements of a sequence and return both the element and respective indices
for index, element in enumerate('abcd'):
    # print(index, element)
    pass

dic = {'a': 0, 'b': 1, 'c': 2, 'd': 4}
tuple_dict = dic.items()

# print(tuple_dict)  # convert dict to tuple

# for key, value in dic.items():
#     print(key, value)

tt = ('a', 0), ('b', 1), ('c', 2), ('d', 4)

dd = dict(tt)  # convert list of tuples into list of dictionaries

# print(dd)

d = dict(
    zip(['doh', 'rae', 'mee'], range(3))
)  # concise way to create a dictionary
# print(d)

directory = {'john': 'cleese', 'peter': 'theil', 'issy': 'jackson'}

number = 1234, 4576, 5679

# for first, last in directory:
#     print(first, last, directory[last, first])

# print(structshape(dic), ">> structshape")



'''Ollie @ 16/10/23 --> https://realpython.com/python-tuple/'''

red = (250, 0, 0)
# print(type(red))

blue = 'Blue' # without a comma, its a string
blue = 'Blue', # with a comma, it becomes a tuple
# print(type(blue))

numbers = tuple(['one', 2, 'three'])
# print(numbers[-1]) # gives me the last element
# print(numbers[-2]) # gives me the second to last element

plane = ({
    "manufacturer": "boeing",
    "model":"747",
    "passengers":416,
}.values())

# print(plane)
this = tuple(x**2 for x in range(11))

# print(len(this)) # will return the number of outputs

# NESTED TUPLE
employee = (
    "John",
    35,
    "Python Developer",
    ("Django", "Flask", "FastAPI", "CSS", "HTML"),
)

# print(employee[-1]) #this returns all elements in the next tuple 
# print(employee[-1][4]) #this returns the last element in the nested tuple in employee i.e. HTML

# SLICING A TUPLE
# --> tuple_object[start:stop:step]

# IMMUTABILITY
# employee[1] = 30
# TypeError: 'tuple' object doesn't support item deletion

student_info = ("Linda", 18, ["Math", "Physics", "History"])
# print(student_info)

# you can manipulate nested mutable elements within a immutable object
student_info[2][2] = "Computer science"
# print(student_info) 

# Packing and Unpacking Tuples

point = (7, 14, 21)

x, y, z = point

# print(x)

new_num = (1, 2, 3, 4, 5)

*head, last = new_num # using the unpacking/packing operator you can assign multiple values to one variable
# print(head, last)

first, *_ = new_num # disposable variables! when you only need one, not all of the variabled from new_num

# print(*point, *new_num) # merging tuples into one by using the * operator to unpack --> returns 7 14 21 1 2 3 4 5

# CONCATENATING AND REPEATING TUPLES


days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

# print(tuple(reversed(days)))

reversed_days = days[::-1]

# print(reversed_days) returns the same as above using the slicing operator[start; stop; step]

# print(id(days) == id(reversed_days)) = FALSE --> no longer share the same id

# sorted(days) # sorts alphabetically

sorted(days) # sorts alphabetically

fruits = (("apple", 0.40), ("banana", 0.25), ("orange", 0.35))

# print(fruits[1][1])

# print(sorted(fruits, key=lambda fruit: fruit[1]))


# TRAVERSING TUPLE IN PYTHON
monthly_incomes = (
    ("January", 5000),
    ("February", 5500),
    ("March", 6000),
    ("April", 5800),
    ("May", 6200),
    ("June", 7000),
    ("July", 7500),
    ("August", 7300),
    ("September", 6800),
    ("October", 6500),
    ("November", 6000),
    ("December", 5500)
    )


total_income = 0
for income in monthly_incomes:
    total_income += income[1]


# print(total_income)



quarter_income = 0

for index, (month, income) in enumerate(monthly_incomes, start=1):
    print(f"{month:>10}: {income}")
    # in the above f-string, the greater than ( > ) symbol indicates how far in an f-string is indented
    quarter_income += income
    if index % 3 == 0:
        print("-" * 20)
        print(f"{'Quarter':>10}: {quarter_income}", end="\n\n")
        quarter_income = 0
        
        