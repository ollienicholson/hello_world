# Any and all

new_list = any([False, False, True])  # True

print(new_list)

new_gen = any(letter == 't' for letter in 'monty')  # True

print(new_gen)

# NOTE: ANY stops as soon as it finds a True value making it more efficient than ALL