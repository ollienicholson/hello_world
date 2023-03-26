# highest and lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

string = "1 2 3 4 25"

string1 = "1 2 -3 4 5"

string2 = "1 9 3 4 10"


# option 1 -submitted
def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return numbers[-1] + ' ' + numbers[0]


print(high_and_low(string))


# option 2
def high_and_low2(numbers):  #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


# option 3
def high_and_low3(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


#  option 4
def high_and_low4(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"


# option 5
def high_and_low5(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))
