from sys import argv
# read the WYSS section for how to run this

script, name = argv
prompt = '>>'

print("\nWelcome to", script + " " + name)
print("\nThis little app will help you generate a random name")
print("\nChoose the name of your first pet:")
first = input(prompt)

print("Choose your favourite flavor of chocolate:")
second = input(prompt)

print("Whats your mothers maiden name")
third = input(prompt)

print("\nThanks for stopping by @", name)

print("\nYour unique name is:", first, second, third)


