# Codewars: reversing using Slicing

n = "Oliver_Nicholson"  # initial string
stringlength = len(n)  # calculate length of the list
slicedString = n[::-1]  # slicing

print(slicedString)  # print the reversed string

## using LOOPS

n = "Oliver_Nicholson"
reversedString = []
index = len(n)  # calculate length of string and save in index
while index > 0:
    reversedString += n[index - 1
                        ]  # save the value of str[index-1] in reverseString
    index = index - 1  # decrement index by 1
print(reversedString)

## using JOIN

s = 'Oliver_Nicholson'  #initial string
reversed = ''.join(
    reversed(s)
)  # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed)  #print the reversed string
