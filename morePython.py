# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years,
# but years divisible by 400 are leap years.
# Tested years are in range 1600 ≤ year ≤ 4000.

def is_leap_year(year):
    return True if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else False

def is_leap_year(year):
    return (year % 100 and not year % 4) or not year % 400

def is_leap_year(year):
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


def noonerize(numbers):
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

def whoseMove(lastPlayer, win):
    players = ['white', 'black']
    return lastPlayer if win else players[players.index(lastPlayer) - 1]

def whoseMove(lastPlayer, win):
    return ["white", "black"][(lastPlayer == "black") == win]

def whoseMove(lastPlayer, win):
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