# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

my_list = 2, 4, 5, 6, 'h', 'n', 2.0

result = [val for val in my_list if isinstance(val, (int, float))]

print(result)

numbers = [val for val in my_list if isinstance(val, (float))]

print(numbers)


def filter_list(list):
    'return a new list with the strings filtered out'
    numbers = [value for value in list if isinstance(value, int)]
    return numbers


print(filter_list(my_list), "print")
