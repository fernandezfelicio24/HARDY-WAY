# DICTIONARIES, OH LOVELY DICTIONARIES


# create a mapping of state ro abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York'  : 'NY',
    'Michigan'  : 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransico',
    'MI': 'Detroit',
    'FL': 'Jacsonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 40)

print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])


#print some states
print('-' * 40)
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('-' * 40)
print("Michigan has : ", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#print every state abbreviation
print('-' * 40)
for state, abbrev in list(states.items()):
    print(f"{state} has the city {abbrev}")
    
#print evry city in state
print('-' * 40)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the {city}")
    
#now do both at the same time
print('-' * 40)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 40)
#safely get a abbreviation by state that might not be there
state = states.get('Texas.')

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")