## ======= Think Python: Ch 10: Exercises =======

# === ex 10-1 ===
# write a function:
# function takes a list of lists of integers and adds up the elements from all of the nested lists
# https://github.com/AllenDowney/ThinkPython2/blob/master/code/list_exercises.py
t = [[1, 2], [3], [4, 5, 6]]

numbers = [1, 2, 3, 4, 5, 1, 4, 5]


def nested_sum(t):
    total = 0
    for item in t:
        # wrapping item in sum helps iterate through a nested list
        total += sum(item)
    return total


print(nested_sum(t))


# === ex 10-2 ===
# function calculates cumulative sum of list
def cumulative_sum(t):
    total = 0
    res = []
    for x in t:
        # total = total + x. Words for lists, not for nested lists
        total += x
        res.append(total)
    return res


print(cumulative_sum(numbers))