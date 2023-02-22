input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.


def open_or_senior(data):
    output = ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]
    return output


print(open_or_senior(input))
