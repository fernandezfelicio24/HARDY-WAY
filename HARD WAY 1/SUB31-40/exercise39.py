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