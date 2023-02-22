t = 'a', 'b', 'c', 'd', 'e', 'f'  # <class 'tuple'>
t1 = ('a', 'b', 'c', 'd', 'e', 'f')  # <class 'tuple'>
t2 = 'a',  # <class 'tuple'> if you throw a comma at the end
numbers = 1, 2, 3, 4, 5, 6

t3 = 'a'  # this is actually <class 'string'> !!
t4 = ('a')  # this is actually <class 'string'> !!

tup = tuple('blah')  # built-in tuple function
# returns ('b', 'l', 'a', 'h')

t = (('A', ) + t[1:])
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

# print(name)
# print(domain)

print(
    divmod(7, 3)
)  # divides 7 by 3, returns results, then returns remainder i.e (7/3 = 2, remainder = 1)

# the following function is a  better way of print divmod, as it saves the quotient to "quot", and saves the remainder to "rem"
# quot, rem = divmod(7, 3) ---> runs in terminal, not in VSCode


def min_max(t: tuple) -> tuple:
    return min(t), max(t)


print(min_max(numbers))
