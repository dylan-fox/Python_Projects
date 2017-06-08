#Imports this script and the file to be edited
from sys import argv
script, filename = argv

#Prompt user to abandon ship or go through with erasing the file
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#opens the file in write mode, and assigns to variable 'target'
print "Opening the file..."
target = open(filename, 'w')

#Truncates the file. Since no parameter is listed, it truncates it to 0.
#print "Truncating the file. Goodbye!"
#target.truncate()

#Opening filename in write mode should erase it.
print "File ready to be rewritten."

#Gets user input for three lines and assigns them to variables.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#Writes the lines to the file, with line breaks inbetween.
print "I'm going to write these to the file."

fulltext = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(fulltext)
"""target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")"""

#Close file, which saves it.
print "And finally, we close it."
target.close()

#Reopens, reads, and closes the new file.
newfile = open(filename)
print "The file now reads:"
print newfile.read()
newfile.close()
