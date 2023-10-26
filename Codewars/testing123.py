# testing 123

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# example:
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    result = []
    for i, line in enumerate(lines, start=1):
        result.append(f'{i}: {line}')
    return result

lines = ["a", "b", "c"]

print(number(lines))  # that works

# Option 2:
def number2(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# Option 3:
def number3(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# Option 4:
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]


# Alternative use cases for enumerate:
items = ['apple', 'banana', 'orange']

for index, items in enumerate(items):
        print(index, items)
        

letters = ['a', 'b', 'c', 'd']
for index, letter in enumerate(letters, start=1):
    print(index, letter)


word = 'Python'
for index, char in enumerate(word):
    print(index, char)