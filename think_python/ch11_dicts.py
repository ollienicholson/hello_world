import numpy as np
from pprint import pp

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError(f'\nValue does not apper in the dictionary')

# reverse lookup is much slower than a forward lookup: if you're working on a large programme, running this function will slow performance

# h = histogram("parrot")
# k = reverse_lookup(h, 2)

# ========================

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#         return inverse

# i = invert_dict(h)

# ========================

# known = {'0: 0', '1: 1'}

# dict = {0: 0, 1: 1, 2: 2}

# def fibonacci(n):
#     if n in known:
#         return known[n]
#     print(known)

#     res = fibonacci(n - 1) + fibonacci(n - 2)
#     known[n] = res
#     print(res, "this")
#     return res

# print(fibonacci(known))

# cant get this to run correctly: TypeError: unsupported operand type(s) for -: 'set' and 'int'.
# ========================

# ===== Think Python: Dictionaries as a collection of counters - Ch. 11, pg. 127 ======
# def histogram(word):
#     dictionary = dict()
#     for char in word:
#         if char not in dictionary:
#             dictionary[char] = 1
#         else:
#             dictionary[char] += 1
#     return dictionary

# ========================

# a = histogram('brontosaurus')

# print(a)

# b = histogram('a')

# print(b)
# print(b.get('a', 1))
# print(b.get('b', 0))

# ===== Think Python: Looping & dictionaries Ch. 11, pg. 128 =====

# def print_hist(h):
#     for c in h:
#         print(
#             c, h[c]
#         )  # c prints the character plus how many times it appears in the word, h represents the entire list

# h = histogram('parrot')
# print_hist(h)

# for key in sorted(h):  # sorts in alphabetical order
#     print(key, h[key])

# ===== Think Python: Global Variables Ch. 11, pg. 133 =====

verbose = False


def example_1():
    if verbose:
        print("running example 1")


been_called = False


def example_2():
    global been_called
    been_called = True


count = 0


def example_3():
    global count
    count += 1


known = {0: 0, 1: 1, 2: 2}

print(known, "this is pre-known")


def example_4():
    # re-assign key-value pair 2:2 so 2 = 1, not 2
    known[2] = 20
    print(known[2], "this is post-known")


example_4()


def example_5():
    global known
    # here we can re-assign known as a variable, choosing to either instatiate known within dict, or simply
    known = dict(known)


example_5()
# print(type(known))
pp(
    known,
    indent=1,
    depth=1,
    width=1,
)
pp(known, depth=1)
pp("this")
