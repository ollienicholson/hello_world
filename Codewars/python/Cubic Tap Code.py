# Cubic Tap Code
# This works similarly to Tap Code except instead of being mapped onto a 5x5 square, letters are mapped onto a 3x3x3 cube, left to right, top to bottom, front to back with space being the 27th "letter". Letters are represented by a series of taps (represented as dots .) and pauses (represented by spaces  ), for example A is represented as . . . (first column, first row, first layer) and   is represented as ... ... ... (third column, third row, third layer).

# For reference the three layers of the cube are as follows (underscore represents space):

# 1  1  2  3 
# 1  A  B  C
# 2  D  E  F
# 3  G  H  I

# 2  1  2  3 
# 1  J  K  L
# 2  M  N  O
# 3  P  Q  R

# 3  1  2  3 
# 1  S  T  U
# 2  V  W  X
# 3  Y  Z  _
# Your task (should you choose to accept it)
# Create two functions encode() and decode(), to encode and decode strings to and from cubic tap code.

# Input
# encode() takes a string of uppercase letters and spaces and outputs a string of dots and spaces. decode() takes a string of dots and spaces and outputs a string of uppercase letters and spaces. All inputs will be valid.

# Examples
# encode("N") => ".. .. .."
# encode("TEST") => ".. . ... .. .. . . . ... .. . ..."

matrix = [[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
[['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
[['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]]



def encode(string):
    print(string)
    result = ""
    for c in string:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if matrix[k][j][i] == c:
                        result +=  (i+1)*'.' + ' ' + (j+1)*'.' + ' ' + (k+1)*'.' + ' '
    return result.strip()



def decode(string):
    list1 = string.split()
    
    result = ""

    for i in range(int(len(list1)/3)):
        
        numdot1 = len(list1[i*3])-1
        numdot2 = len(list1[i*3+1])-1
        numdot3 = len(list1[i*3+2])-1
    
        result += matrix[numdot3][numdot2][numdot1]
        
    return(result)

