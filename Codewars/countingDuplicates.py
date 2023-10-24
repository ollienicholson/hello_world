text = "invisibilities"

def duplicate_count(text):
    text = text.lower()
    dict = {}
    duplicates = 0
    for letter in text:
        dict[letter] = dict.get(letter, 0) +1
    for letter, amount in dict.items():
        if amount > 1:
            duplicates += 1
    return duplicates

print(duplicate_count(text))
