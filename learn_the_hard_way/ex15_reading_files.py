from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

# =========================================

## another useful example of using sys.argv

# Python program to demonstrate command line arguments 

# when running this script - make sure you add in a set of variables as your argv inputs


# import sys

# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)

# # Arguments passed
# print("\nName of Python script:", sys.argv[0])

# print("\nArguments passed:", end=" ")
# for i in range(1, n):
#     print(sys.argv[i], end=" ")

# # Addition of numbers
# Sum = 0

# for i in range(1, n):
#     Sum += int(sys.argv[i])

# print("\n\nResult:", Sum)

# =========================================