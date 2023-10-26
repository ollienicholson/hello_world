# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# example:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(a1, a2):
    longest = ''.join(sorted([l for l in set(a1 + a2)]))
    return longest


def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# print(longest(a, b))
# print(longest2(a, b))
