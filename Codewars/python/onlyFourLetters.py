# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.


# check if each name has <= 4 chars, if so include in list
friends = ["Ryan", "Kieran", "Mark"]

def checkName(names):
    return [i for i in names if len(i) <= 4]
# almost although your frined list needxs to equal exactly 4 chars
# below is the accepted solution


def friend(names):
    return [i for i in names if len(i) == 4]

print(friend(friends))