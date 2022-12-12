from sys import argv

script, filename = argv

print(f"\nWe're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you DO want that, hit RETURN.")

input("\nWhat do you say??")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file, goodbyeee!")
target.truncate()

print("Now im going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"And finally, we close the {filename} file.")

target.close()