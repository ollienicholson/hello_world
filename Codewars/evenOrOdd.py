# returns "even" if number is even, and "Odd" if the number is odd


# 1 explicit
def even_or_odd_0(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 2 return in one line
def even_or_odd_1(number):
    return 'Odd' if number % 2 else 'Even'


def even_or_odd_2(number):
    return 'Even' if number % 2 == 0 else 'Odd'


# using square brackets
def even_or_odd_3(number):
    return ["Even", "Odd"][number % 2]


print(even_or_odd_0(3))