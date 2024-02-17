# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

# long/slow version
def invert(lst):
    invert = []
    for i in lst:
        invert.append(i-i*2)
    return invert

# refectored version
def invert2(lst):
    return [i - i * 2 for i in lst]

# you can also do
def invert3(lst):
    return [-x for x in lst]