# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5

#  my first solution was...
import math
def litres(time):
    return math.floor(time / 2)

# then I learned you can you "//" as an alternative to math.floor
def litres2(time):
    return time // 2

# alts
def litres3(time):
    return int(time*0.5)