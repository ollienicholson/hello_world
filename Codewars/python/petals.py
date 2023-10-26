# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# f1 = even
# f2 = odd
# return true if f1 = false and f2 = odd
flowers = 5, 8

# def number(num):
#     return True if num % 2 == 0 else False


def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    return False


print(lovefunc(3, 3))
print(lovefunc(2, 3))
print(lovefunc(3, 2))
print(lovefunc(2, 2))

# print(number(6))