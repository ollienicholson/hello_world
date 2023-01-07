
# ===== Learn Python: Dictionaries as a collection of counters - Ch. 11, pg. 127 ======
def histogram(word):
    dictionary = dict()
    for char in word:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary


# a = histogram('brontosaurus')

# print(a)

# b = histogram('a')

# print(b)
# print(b.get('a', 1))
# print(b.get('b', 0))

# ===== Learn Python: Looping & dictionaries Ch. 11, pg. 128 =====

def print_hist(h):
    for c in h:
        print(
            c, h[c])  # c prints the character plus how many times it appears in the word, h represents the entire list


h = histogram('parrot')
# print_hist(h)

for key in sorted(h):  # sorts in alphabetical order
    print(key, h[key])
