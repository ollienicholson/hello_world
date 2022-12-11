# this is how a list functions; you call data using only numbers e.g. [1]

# things = ['a', 'b', 'c', 'd']

# print(things[1])

# things[1] = 'z'
# print(things[1])

# print(things)
# print('\nthe above is a list')

# now lets compare the above to a dictionary or 'dict'

# stuff = {'name': 'Oliver', 'age': 34, 'height': 6 * 12 + 2}

# print(stuff['name'])

# print(stuff['age'])

# print(stuff['height'])

# stuff['city'] = 'AKL'

# print(stuff['city'])

# print(stuff)

# stuff[1] = "Wow"
# stuff[2] = "Holy Shit"

# print(stuff[1])
# print(stuff[2])

# print(stuff, ' now with the added words')

# print('\ndeleting things...')
# del stuff['city']
# del stuff[1]
# del stuff[2]
# print(stuff)

# ====== now lets run an exercise pg. 161

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco', 'MI': 'Detriot', 'FL': 'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('- ' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('- ' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# print some states using the state then city dict
print('- ' * 20)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('- ' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('- ' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('- ' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# safely get an abbreviation by state that might not be there
print('- ' * 10)
state = states.get('Texas')
if not state:
    print("sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

# practice the studydrills

# learn about collections.OrderedDict