
name = 'Oliver Nicholson'
age = 34

height = 1.82    # metres
# convert metres into feet
feet = 1 * 3.28084

weight = 70      # kgs
# convert kilos into pounds
pounds = 1*2.2

eyes = 'green'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {round(height*feet)} feet tall.")
print(f"He's {weight*pounds} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usualy {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")
