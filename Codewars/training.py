# def square_sum(numbers):
#     #your code here
#     sum = 0
#     for i in numbers:
#         sum += i * 2
#     return sum

# print(square_sum([3]))


def squre_me(numbers):
    result = sum([num**2 for num in numbers])
    return result


print(squre_me([5, 10]))


# =======

name = "sam harris"


def func(i):
    return ".".join(word[0].upper() for word in i.split())


func(name)