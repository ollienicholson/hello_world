# You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

age = "2 years old"


def get_age(age):
    return int(age[:1])

    # slice a string to get (and return) the first character


string = "string"

print(string[:1])

print(string[1])

print(get_age(age))
