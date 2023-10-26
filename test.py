# import numpy as np

def function(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


# print(function(2, 1))

my_tuple = 1, 2, 3, 4, 5

my_list = [2, 4, 6, 8, 10]

my_dict = {
    "One": "1",
    "Two": "2",
    "Three": "3",
}


# === playing around with loops ===
def loop(items):
    result = sum([i * i for i in items])
    print(items, "this is i")
    print(result, "this is post-i")
    return result


def new_loop(items):
    items.reverse()
    items.append(20)
    items.pop(0)


print("hello world")
