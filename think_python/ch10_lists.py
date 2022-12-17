# from think_python import list_examples

import numpy as np

# ============= Learn Python: Chapter 10, Pg 107 exercises =============

t = [['one', 'two', 'three', 'four', 'Five', 'Six']]
a_list = ["a", "b", "c", "d", "e", "f"]
b_list = ["a", "b", "c", "d", "e", "f"]

upper = ["ONE", "TWO", "three"]
string = '   peterpan'
n = [1, 2, 3, 4, 5]
p = [10, 2, 7, 4, 5]
# m = ["TEAM"]


def add_all(n):
    # type: (list) -> (list)
    total = 0
    for x in n:
        total += x
    return total


# print("Add all:", add_all([2, 2]))

# def capitalise_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

# print("Capitalise all:", capitalise_all(t))

# = = =


def only_upper(upper):
    # this function only returns elements which are all UPPERCASE
    list = []
    for item in upper:
        if item.isupper():
            list.append(item)
    print(list)
    # == this function returns the "list" of all uppercase elements in the list
    # list is only utilised within this function
    # outside of this function, the variable 'list' can not be accessed
    return list


# print("\nPrinting t: ", t)

# print(only_upper(upper))

# = = =

# ======= page 113 =======
# words = "The hills are alive"

# words2 = words.split()
# print(words2)

# a = "spam.spam.spam"

# this = "."
# b = a.split(this)

# print(b)

# end = " "

# newwords = end.join(words2)

# print(newwords)

# == DELETING ITEMS ==
# two identical variables create the same object, the answer to the below should be TRUE
one = "banana"
two = "banana"

print("Are VAR 'one' and 'two' the sanme? ", one is two)
# two identical lists create two objects therefore the below answer should = FALSE
print("are a_list and b_list LISTS the same? ", a_list is b_list)

print(a_list)  # list before any changes
x = a_list.pop(1)  # remove element (index of 1) from list
print(a_list)  # print list after changes
print(x)  # print removed element from list

print(a_list[0])  # print current index of 0
del a_list[0]  # remove index 0

print(a_list)  # print list after changes

a_list.remove('f')  # remove 'f'

print(a_list)

print("This is a copy of a_list:", a_list[:])

print("this is b_list:", b_list)
spacer = " "
c_list = spacer.join(b_list)

print("\nThis is the effect of function .join on b_list: ", c_list)

print("Are b_list and c_list the same?", b_list is c_list)

n = p
print("\nare n & p lists the same?", n is p)
print("These two lists are alised")
n[0] = 25
print("changing the alised object will change the other:", p)


# ==== List Arguments ===
def delete_head(x):
    del x[0]
    return


delete_head(b_list)
print(b_list)

z = n + ["a", 10]
print(z)


def tail(t):
    return t[1:]


last = tail(n)
print("We just chopped the end off 'n': ", last)

print("List before .strip: ", string)

string = string.strip()

print(string)
print("\nthis is 'n' before sorting:", n)
n.sort()
print("this is 'n' after sorting", n)
n = n.sort()
print(
    "this is the WRONG way to sort the list 'n', as it returns nothing: >> ", n
)

print(p)
sorted = sorted(p)

print(sorted)