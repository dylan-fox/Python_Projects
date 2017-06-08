from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#We could do these two on one line, how?
#Assign the variable in_file to be the original file.
in_file = open(from_file)
#Assign the variable indata to be the text of the original file by reading in_file.
indata = in_file.read()
#Calculate the length of the indata string. (Optional)
length = len(indata)

"""
#Confirm input file length & operation go-ahead
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
"""

#Open the to file in write mode (clearing it), then assign to variable out_file
out_file = open(to_file, 'w')
#Write the contents of the from file in the to file.
out_file.write(indata)

#Inform user.
print "You copied %d bytes from %r to %r." %(length, from_file, to_file)

#Close files, saving them.
out_file.close()
in_file.close()
