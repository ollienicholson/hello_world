from collections import defaultdict

d = defaultdict(list)
print(d, "d")

t = d["new key"]
print(t, "t")

t.append('new value')

print("\n", d, "new d")


def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


print(
    signature('hello my friend!')
)  # returns the string as sorted letters: '!deefhilmnory'

text = '   hello kind sir   '
print(
    text.strip()
)  # returns the string without the whitespace: 'hello kind sir'


# 1: original function
def all_anagrams(filename) -> dict:
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


# 2: using setdefault
def all_anagrams2(filename) -> dict:
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d.setdefault(t, []).append(word)
    return d


# print(all_anagrams2('words.txt'))


# 3: using defaultdict
def all_anagrams3(filename) -> dict:
    d = defaultdict(list)  # create a defaultdict that returns an empty list
    for line in open(filename):  # open file andread each line
        word = line.strip().lower()  # strip whitespace and lowercase e.g. 'hello'
        t = signature(word)  # get the signature of the word (sorted letters) as the key e.g. 'ehllo'
        d[t].append(
            word
        )  # append the word to the list of words with this signature

    return d


print(all_anagrams3('words.txt'))
