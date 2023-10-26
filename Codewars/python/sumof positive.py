# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.
def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
    return sum

# -- other options --
def positive_sum(arr):
    return sum(number for number in arr if number > 0)


import functools

def positive_sum(arr):
    return functools.reduce(lambda accumulator, current: accumulator + (current if current > 0 else 0), arr, 0)