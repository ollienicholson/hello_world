t = 'a', 'b', 'c', 'd', 'e', 'f',  # <class 'tuple'>
t1 = ('a', 'b', 'c', 'd', 'e', 'f')  # <class 'tuple'>
t5 = ('a', 'b', 'c', 'd', 'e', 'f')  # <class 'tuple'>
t2 = 'a',  # <class 'tuple'> if you throw a comma at the end
numbers = 1, 2, 3, 4, 5, 6

t3 = 'a'  # this is actually <class 'string'> !!
t4 = ('a')  # this is actually <class 'string'> !!

tup = tuple('blah')  # built-in tuple function
# returns ('b', 'l', 'a', 'h')

# t = (('A', ) + t[1:])
# this function makes a new tuple and makes t refer to it, replacing 'a' with 'A'
(0, 1, 2) < (0, 3, 4)
# returns True

(0, 1, 2000) < (0, 3, 4)
# travereses though the elements until it finds two elements that differ i.e 2000 < 4, still returns True as these subsequent numbers are not considered.. weird right?

a, b = 1, 2
# a = 1, b = 2

a, b = 'b', 'a'
# a = 'b', b = 'a'

addr = 'ollie.nicholson@gmail.com'
name, domain = addr.split('@')  # returns ollie.nicholson, gmail.com

# print(
#     divmod(7, 3), ">> divmod example 1"
# )  # divides 7 by 3, returns results, then returns remainder i.e (7/3 = 2, remainder = 1)

# the following function is a  better way of print divmod, as it saves the quotient to "quot", and saves the remainder to "rem"
quot, rem = divmod(7, 3)  #---> runs in terminal, not in VSCode

# print(quot, rem, "quot & rem")


def min_max(t: tuple) -> tuple:
    return min(t), max(t)


# print(min_max(numbers))


# "*args" gathers all arguments into a tuple
def printall(*args):
    print(*args)


# print(printall(1, 2.0, '3'), "*args unpacks all")

# using '*' we 'scatter' the tuple in order to pass it into divmod
a = 7, 3

# print(divmod(*a))


# sumall takes any number of arguments and returns their sum
def sumall(*args):
    return sum(*args)


# print(sumall(a))

# "zip" combines two or more sequences a returns a list of tuples (kinda like a dict), where each tuple contains one element from each sequence.
# the resutling key-value pairs are easily accessed via a 'for' loop
# the for loop will only execute elements which correspond to one another. If one sequence is longer than the other, the additional elements will not be accessed.

# print(zip(t, numbers), "zip ex1")

# for pair in zip(t, numbers):
#     print(pair)

# print(zip('abcdef', range(3), range(4)), "zip ex2")

# for kvp in zip('abcdef', range(3), range(4)):
#     print(kvp)

# print(list(zip(t, numbers)), "zip the list")

z = list(zip(t, numbers))

# unpack elements with a for loop
# for letter, number in z:
#     print(letter, number)


def has_match(tup1, tup2):
    for x, y in zip(tup1, tup2):
        if x == y:
            return True
        return False


print(has_match(t1, t))

#  traverse through elements of a sequence and return both the element and respective indices
for index, element in enumerate('abcd'):
    print(index, element)