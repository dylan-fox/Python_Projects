from sys import argv
#Take an input file from system
script, input_file = argv

#Function that runs the read command on what gets passed to it
def print_all(f):
    print f.read()

#Function that sets argument's position to 0
def rewind(f):
    f.seek(0)

#Prints the line at the current position in the file
def print_a_line(line_count, f):
    print line_count, f.readline(),

#Open the input file, assign to variable current_file
current_file = open(input_file)

#Prints file
print "First let's print the whole file: "
print_all(current_file)

#Rewinds file (sets position back to 0)
print "Now let's rewind, kind of like a tape."
rewind(current_file)

#Prints lines one at a time, incrementing current_line value each time
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)
