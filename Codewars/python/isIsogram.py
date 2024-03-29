# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)


def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            return False
    return True


print(is_isogram("heLlo"))
print(is_isogram("true"))


def is_isogram(string):
    return len(string) == len(set(string.lower()))


def is_isogram(string):
    s = set(string.lower())
    if len(s) == len(string):
        return True
    return False