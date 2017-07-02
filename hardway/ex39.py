#Create mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '-'*10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-'*10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)

#print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

#now do both simultaneously
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '-'*10
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

#Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city


#How about a character dictionary?
Robin = {'class': 'wizard', 'race': 'halfling', 'subrace': 'lightfoot', 'familiar': 'perk'}
print Robin
#Convenient methods:
#'del' - deletes key and value, given key
del Robin['subrace']

#'.keys()' - lists keys for a dictionary
print Robin.keys()
print sorted(Robin.keys())

#'in' - checks whether a dic has a certain key
print 'race' in Robin

#'dict' - builds a dictionary from a list of pairs
Lara = dict([('class', 'cleric'), ('race', 'human'), ('deity', 'Shelyn')])

#You can also use dict with simple assignments:
Grigori = dict(charClass='Inquisitor', race='Half-Orc', deity='Abadar')
