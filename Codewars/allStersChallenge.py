# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0


def str_count(string, letter):
    # pass a string and a character
    return string.count(letter) if letter in string else 0
    # give me a count of character in string
    # return the count as an int if char in str else return 0


string = "hello"
char = 'l'

print(str_count(string, char))

# option B
def strCount(string, letter):
    return string.count(letter)

# option C

strCount = str.count

print(strCount(string, char))
