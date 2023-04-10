# Using conditional expressions

import math

x = 3

# Example 1:
#  here we use a conditional statement

if x > 0:
    y = math.log(x)
else:
    y = float('nan')

print(y)
# we can make this more concise using a conditional expression

y = math.log(x) if x > 0 else float('nan')


# Example 2:
# conditional statement
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# conditional expression
def factorial_new(n):
    return 1 if n == 0 else n * factorial(n - 1)
