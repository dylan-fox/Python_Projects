"""
#Using a simple while loop:
i = 0
numbers = []

while i < 6:
    print "At the top of i is %d" %i
    numbers.append(i)

    i = i+1
    print "Numbers now: ", numbers
    print "At the bottom i is %d \n" %i

print "The numbers: "

for num in numbers:
    print num
"""

"""
#Making it into a function that accepts length and increment:
def listMaker(len, increment):
    i = 0
    numbers = []
    while i < len:
        print "At the top of i is %d" %i
        numbers.append(i)

        i = i+increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d \n" %i

    print "The numbers: "

    for num in numbers:
        print num
"""

#Rewriting using for loops:
def listMaker(len, increment):
    numbers = []

    for i in range(len):
        print "At the top of i is %d" %i
        numbers.append(i)
        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d \n" %i

        print "The numbers: "

    for num in numbers:
        print num
#Looks like the for loop resets the increment every time. Can't mess with it from inside the loop.
