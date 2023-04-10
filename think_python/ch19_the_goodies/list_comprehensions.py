# using 'Map, Filter, and Reduce' within list comprehension

# heres the original function


# MAP: mapping the string method capitalize to the elements of the list
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


# here is the list comprehension version


def capitalize_all(t):
    return [s.capitalize() for s in t]


# FILTER: upper

this = "a", "B", "c", "D", "e"


# orginal function
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


print(only_upper(this))


def only_upper_new(t):
    return [s for s in t if s.isupper()]


print(only_upper_new(this))