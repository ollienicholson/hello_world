# ten_things = "\nApples Oranges Crows Telephone Light Sugar"

# print('\n', ten_things)

# print("\nWait there are not 10 things in that list. Let's fix that.")

# stuff = ten_things.split(' ')
# more_stuff = ['Day', 'Night', 'Song',
#               'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

# print("\nThere we go:", stuff)

# print("Let's do some things with 'stuff'.")

# # print the second item in the list
# print(stuff[1])
# # print the 3rd from last
# print(stuff[-3])  # fancy!!
# print(stuff.pop())
# print(" ".join(stuff))
# print("#".join(stuff[3:6]))

# # other examples of scripts which could use lists:
# # family tree
# # deck of cards
# # counting from 0 - 100
# # top 10 movies
# # top 10 car manufacturers
# # top 10...anything

t = ['one', 'two', 'three', 'four', 'Five', 'Six']
n = [1, 2, 3, 4, 5]


def add_all(n):
    total = 0
    for x in n:
        total += x
    return total


print("Add all:", add_all(n))


def capitalise_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


print("Capitalise all:", capitalise_all(t))


def only_upper(t):
    res = []
    print(res)
    for s in t:
        if s.isupper():
            res.append(s)
    print(res)
    return res


print(t)
