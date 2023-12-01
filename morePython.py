# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years,
# but years divisible by 400 are leap years.
# Tested years are in range 1600 ≤ year ≤ 4000.

def is_leap_year(year):
    return True if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else False

def is_leap_year(year):
    return (year % 100 and not year % 4) or not year % 400

def is_leap_year(year):
    return True if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else False


# Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway! If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do check it out first.

# You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or 0 if the numbers are equal:

# [123, 456] = 423 - 156 = 267
# Your code must test that all array items are numbers and return "invalid array" if it finds that either item is not a number. The provided array will always contain 2 elements.

# When the inputs are valid, they will always be integers, no floats will be passed. However, you must take into account that the numbers will be of varying magnitude, between and within test cases.

def noonerize(numbers):
    try:
        num1 = int(str(numbers[1])[0] + str(numbers[0])[1:])
        num2 = int(str(numbers[0])[0] + str(numbers[1])[1:])
    except ValueError:
        return "invalid array"
    return abs(num1 - num2)


def noonerize(numbers):
    if not all(isinstance(n, int) for n in numbers):
        return 'invalid array'
    a, b = map(str, numbers)
    return abs(int(a[0] + b[1:]) - int(b[0] + a[1:]))
