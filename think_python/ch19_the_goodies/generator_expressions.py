# Generator expressions
# NOTE: generator expressions are similar to list comprehension except are surrounded by parentheses, not square brackets

generator = (x**2 for x in range(10))

# print(generator)
# print(next(generator))

for value in generator:
    print(value)

# Generator expressions are often used with functions like 'sum', 'max' and 'min'

new_sum = sum(x**2 for x in range(5))

print("\n", new_sum)