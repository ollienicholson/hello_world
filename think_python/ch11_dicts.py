import numpy as np


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError(f'\nValue does not apper in the dictionary')


# reverse lookup is much slower than a forward lookup: if you're working on a large programme, running this function will slow performance

h = histogram("parrot")
k = reverse_lookup(h, 2)

# ===== CODE WARS exercise =====
name = "sam harris"


def func(i):
    return ".".join(word[0].upper() for word in i.split())


func(name)

# ========================


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
        return inverse


i = invert_dict(h)

# ========================

known = {'0: 0', '1: 1'}

dict = {0: 0, 1: 1, 2: 2}


def fibonacci(n):
    if n in known:
        return known[n]
    print(known)

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    print(res, "this")
    return res


print(fibonacci(known))
# cant get this to run correctly: TypeError: unsupported operand type(s) for -: 'set' and 'int'.
# ========================
