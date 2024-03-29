# ex18, pg 83

# this one is like your scripts with argv


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that arg is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print(1 + 1)


def print_none():
    print(5)


print_two('Oliver', 'Nicholson')

print_two_again("One", "Two")

print_one("First!!")

print_none()