# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years,
# but years divisible by 400 are leap years.
# Tested years are in range 1600 ≤ year ≤ 4000.


def is_leap_year(year):
    return True if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else False

def is_leap_year_2(year):
    return (year % 100 and not year % 4) or not year % 400

def is_leap_year_3(year):
    return True if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else False


# Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway! If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do check it out first.
# You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or 0 if the numbers are equal:
# [123, 456] = 423 - 156 = 267
# Your code must test that all array items are numbers and return "invalid array" if it finds that either item is not a number. The provided array will always contain 2 elements.
# When the inputs are valid, they will always be integers, no floats will be passed. However, you must take into account that the numbers will be of varying magnitude, between and within test cases.

def noonerize(numbers):
    try:
        num1 = int(str(numbers[1])[0] + str(numbers[0])[1:])
        num2 = int(str(numbers[0])[0] + str(numbers[1])[1:])
    except ValueError:
        return "invalid array"
    return abs(num1 - num2)


def noonerize_2(numbers):
    if not all(isinstance(n, int) for n in numbers):
        return 'invalid array'
    a, b = map(str, numbers)
    return abs(int(a[0] + b[1:]) - int(b[0] + a[1:]))


# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# Note: You can expect all of the inputs to be the same length.

def triple_trouble(one, two, three):
    zipped = zip(one, two, three)
    # this is an awesome example of using list comprehension to wrap a nested for loop
    # this is a more concise way of writing nested for loops in the case of multi layered data structures
    flattened = [char for tup in zipped for char in tup]
    return ''.join(flattened)

# alts
def triple_trouble_2(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))

def triple_trouble_3(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))


# Two players - "black" and "white" are playing a game. The game consists of several rounds. If a player wins in a round, he is to move again during the next round. If a player loses a round, it's the other player who moves on the next round. Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.

# Input/Output
# [input] string lastPlayer/$last_player
# "black" or "white" - whose move it was during the previous round.
# [input] boolean win/$win
# true if the player who made a move during the previous round won, false otherwise.
# [output] a string
# Return "white" if white is to move on the next round, and "black" otherwise.
# Example
# For lastPlayer = "black" and win = false, the output should be "white".
# For lastPlayer = "white" and win = true, the output should be "white".

def whose_move(last_player, win):
    if last_player == "black" and not win or last_player == "white" and win:
        return "white"
    else:
        return "black"
    
# alts
def whoseMove(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'

def whoseMove_2(lastPlayer, win):
    players = ['white', 'black']
    return lastPlayer if win else players[players.index(lastPlayer) - 1]

def whoseMove_3(lastPlayer, win):
    return ["white", "black"][(lastPlayer == "black") == win]

def whoseMove_4(lastPlayer, win):
    if lastPlayer == 'black':
        if win == True:
            return 'black'
        else:
            return 'white'
    else:
        if win == True:
            return 'white'
        else:
            return 'black'



# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
def repeats(arr):
    z = [x for x in arr if arr.count(x) == 1]
    return z[0] + z[1]

# alts
from collections import Counter

def repeats_2(arr) -> int:
    element_count = Counter(arr)
    unique_e = [element for element, count in element_count.items() if count == 1]
    return unique_e[0]+unique_e[1]


# You're given a two-dimensional array of integers matrix. Your task is to determine the smallest non-negative integer that is not present in this array.
# Input/Output
# [input] 2D integer array matrix
# A non-empty rectangular matrix.
# 1 ≤ matrix.length ≤ 10
# 1 ≤ matrix[0].length ≤ 10
# [output] an integer
# The smallest non-negative integer that is not present in matrix.
matrix = [[4, 5, 3, 21, 3, 8],
            [2, 2, 6, 5, 10, 9],
            [7, 5, 6, 8, 2, 6],
            [1, 4, 7, 8, 9, 0],
            [1, 3, 6, 5, 5, 1],
            [2, 7, 3, 4, 4, 3]]

import numpy as np
matrix_np = np.array([[4, 5, 3, 21, 3, 8],
            [2, 2, 6, 5, 10, 9],
            [7, 5, 6, 8, 2, 6],
            [1, 4, 7, 8, 9, 0],
            [1, 3, 6, 5, 5, 1],
            [2, 7, 3, 4, 4, 3]])

def smallest_integer(matrix):
#   to flatten a 2D matrix we loop over matrix and then over item wrapped in list comprehension
    flat = [item for list in matrix for item in list]
#   put the list into a set for fast iteration
    elements_set = set(flat)
#   set a while loop to iterate through non-negative numbers
    missing_integer = 0
    while missing_integer in elements_set:
        missing_integer += 1
    return missing_integer

# alts
# 
# IMPORTANT NOTE ON SUM
# 
# nums = set(sum(matrix, []))
# 
# The sum() function is typically used to add numbers together, but it can also be used to concatenate lists. 
# In this context, sum() is used to flatten the matrix from a list of lists into a single list. 
# It starts with the second argument [] (an empty list) and adds elements of matrix to it.

# For example, if matrix is [[1, 2], [3, 4]], the sum() call will do the following:

# Start with an empty list: []
# Add the first sublist: [] + [1, 2] = [1, 2]
# Add the second sublist: [1, 2] + [3, 4] = [1, 2, 3, 4]
# So after this call, we would have a single list [1, 2, 3, 4].

# The set() function THEN takes an iterable and returns a new set object, a collection of unordered unique elements. 
# By passing the flattened list to set(), you're converting the list to a set, which removes any duplicate elements.

# Continuing with the above example, if the flattened list was [1, 2, 3, 4, 1], converting it to a set would result in {1, 2, 3, 4}. Note that in a set, the order of the elements is not guaranteed.

def smallest_integer_2(matrix):
    # nums = set(sum(matrix, []))
    nums_2 = set(matrix.flatten())
    print(nums_2)
    n = 0
    # while n in nums: n += 1
    while n in nums_2: n += 1
    return n

print(smallest_integer_2(matrix_np))


from itertools import filterfalse, chain, count
def smallest_integer_3(matrix):
    return next(filterfalse(set(chain.from_iterable(matrix)).__contains__, count()))


def smallest_integer_4(matrix):
    i=0
    while np.isin(i,matrix):
        i+=1
    else:
        return i

