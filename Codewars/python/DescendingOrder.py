num1 = 12345
num2 = 18364
num2List = [18364]


def descending_order(num):
    # Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
    # Essentially, rearrange the digits to create the highest possible number.

    # return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))
    # return "".join(map(str, sorted([i for i in str(num)], reverse=True))) # still runs
    # return "".join(sorted([i for i in str(num)], reverse=True)) # still runs
    return int("".join(sorted([i for i in str(num)], reverse=True)))


def descending_order2(num):
    return int("".join(sorted(str(num), reverse=True)))


def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)


print(descending_order(num1))

sorted([i for i in str(num2)]
       )  # returns ['1', '3', '4', '6', '8', '[', ']'] for [18364]

sorted(i for i in str(num2))  # returns ['1', '3', '4', '6', '8'] for 18364

# sorted(i for i in num2)  # returns TypeError: 'int' object is not iterable

print(descending_order2(57483))