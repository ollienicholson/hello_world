# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo"
# name + " does not play banjo"

# Names given are always valid strings.

# 1. function passes a string
# 2. function reads if not upper or lowercase r,
# first we want to return true if r
# else return false

# then we want to return string

name = 'Regan'
name3 = 'regan'
name2 = 'ollie'
name4 = 'Ollie'
# output = ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]


def banjo(name):
    return (
        name + " plays banjo" if name[0] == 'r' or name[0] == 'R' else name +
        " does not play banjo"
    )
def banjo_2(name):
    if name[0] == 'r':
        return name + " plays banjo"
    elif name[0] == 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print(banjo(name))
print(banjo(name3))
print(banjo(name2))
print(banjo(name4))
