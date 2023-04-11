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


# print(only_upper(this))


def only_upper_new(t):
    return [s for s in t if s.isupper()]


# print(only_upper_new(this))

my_tuple = (1, 2, 3, 3, 4, 5, 5)
my_set = set(my_tuple)

print(my_set)
# RETURNS {1, 2, 3, 4, 5}
# NOTE: the set function removes duplicates

    # see sets.py for more info
