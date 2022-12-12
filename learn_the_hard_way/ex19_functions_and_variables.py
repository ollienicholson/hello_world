#page 87


def cheese_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print(f"Man that's enough for a party!")
    print(f"Get the blanket. \n")


print("We can just give the function the numbers directly:")
cheese_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and the math:")
cheese_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def something(a, b):
    c = [1, 2, 3, 4, 5]
    d = 'a', 'b', 'c'
    print("This will give you: ", a + b + a + b)
    print("And this will give you: ", b + c)


something(1, 2)
