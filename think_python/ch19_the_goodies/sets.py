# SETS:
# using sets we can rewrite functions concisely and efficiently

# Example 1:
# SUBTRACT
def subtract(d1, d2):
    """Return a set of all elements in d1 that are not in d2."""
    res = []
    for x in d1:
        if x not in d2:
            res.append(x)
    return res


def subtract_new(d1, d2):
    """Return a set of all elements in d1 that are not in d2."""
    return set(d1) - set(d2)

# Example 2:
# HAS DUPLICATES
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates_new(t):
    return len(set(t)) < len(t)

# Example 3:
# USES ONLY
def uses_only(word, available):
    """Returns True if the word contains only letters in available."""
    for letter in word:
        if letter not in available:
            return False
    return True

def has_only_new(word, available):
    """Returns True if the word contains only letters in available."""
    return set(word) <= set(available)