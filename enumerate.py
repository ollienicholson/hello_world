'''Ollie @ 16/10/23 https://realpython.com/python-enumerate/'''



values = ["a", "b", "c", 'd']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def values1():
    for value in values:
        print(value)

# values1()
# print('\n')

index = 1

def values2():
    index = 1
    for value in values:
        print(index, value)
        index += 1


# USING RANGE & LEN
# using range & len we remove the need for a counter
def values3():
    for index in range(len(values)):
        value = values[index]
        print(index, value)
        

# USING ENUMERATE
# for count, value in enumerate(values):
#     print(count, value)
    
    
# for count, value in enumerate(values, start=1):
#     print(count, value)


def even_items(iterable):
    """Return items from ``iterable`` when their index is even."""
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values

# a more pythonic way of the above even_items function
def even_items_1(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

# print(even_items_1(numbers))



# UNDERSTANDING ENUMERATE A LITTLE MORE

def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

seasons = ["Spring", "Summer", "Fall", "Winter"]
print(my_enumerate(seasons)) # returns <generator object my_enumerate at 0x00000299B858AF90>

print(list(my_enumerate(seasons)), '\n') # returns [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]