# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


def count1(inputStr):
    return sum([inputStr.count(c) for c in "aeiou"])


def count2(inputStr):
    num_vowels = 0
    for vow in ["a", "e", "i", "o", "u"]:
        num_vowels += inputStr.count(vow)
    return num_vowels


def count3(s):
    return sum(c in 'aeiou' for c in s)


print(count1('ael'))

print(count2('ael'))