#Sets x as a string featuring a decimal number of types of people.
x = "there are %d types of people." %10

#Set strings as variables.
binary = "binary"
do_not = "don't"

#Write joke, incorporating earlier defined strings.
#String inception
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#Print strings x and y, using anything for x and a string for y.
#String inception
print "I said: %r." %x
#String inception
print "I also said: '%s'." %y

#set the hilarious boolean.
hilarious = False

#Set the joke evaluation to be a string awaiting a value.
joke_evaluation = "Isn't that joke so funny?! %r"

#Combine joke evaluation with the boolean set earlier.
#String inception
print joke_evaluation % hilarious

#Set two strings and then combine them in print.
w = "This is the left side of..."
e = "a string with a right side."
print w + e
