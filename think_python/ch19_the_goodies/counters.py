# Counters

from collections import Counter

count = Counter('Parrot')

# print(count) # Counter({'r': 2, 'P': 1, 'a': 1, 'o': 1, 't': 1})

# print(count['d']) # 0


# rewriting isAnagram
def isAnagram(word1, word2):
    return Counter(word1) == Counter(word2)


# print(isAnagram('parrot', 'torrap'))  # True
# print(isAnagram('god', 'dog'))  # True

for val, freq in count.most_common(
):  # most_common() returns a list of (n)most common tuples
    print(val, freq, ">>")  # r 2, P 1, a 1,

for val, freq in count.items():  # items() returns a list of tuples
    print(val, freq)  # r 2, P 1, a 1, o 1, t 1,
