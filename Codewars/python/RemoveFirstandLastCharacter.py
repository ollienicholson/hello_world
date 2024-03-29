def remove_char(s):
    a = s[:-1]
    b = a[1:]
    return b

text = 'eloquent'
print(remove_char(text))

# other solutions --

def remove_char1(s):
    return s[1 : -1]

def remove_char2(s):
    return '' if len(s) <= 2 else s[1:-1]

def remove_char3(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)