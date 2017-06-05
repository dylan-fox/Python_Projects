#Import argument values from the command line.
from sys import argv

#Accept two arguments: this script and a filename.
script, filename = argv

#Set a variable txt to be the file you imported.
txt = open(filename)

#Print out a message and the filename.
print "Here's your file: %r" %filename
#Print the contents of the variable txt, which is the file you imported.
print txt.read()


#Ask the user to type the filename again.
print "Type the filename again:"
#Set a variable to be the name of the file they typed.
file_again = raw_input("> ")

#Set a new variable to be the file itself.
txt_again = open(file_again)

#Print the text of the file.
print txt_again.read()

txt.close()
txt_again.close()

"""
Note: Demanding the file in the command line is smoother,
but requires the user to know what arguments they need to pass.
"""

"""
Further note: to open the sample in the python shell, you should:
1) run 'python' in powershell/command line to get into a python shell
2) import os, then run cwd = os.getcwd() to learn current working directory
3) type variable = open("ex15_sample.txt")
4) type print variable.read()
5) use quit() to get out of the python shell

Only 3 and 4 are really necessary.
"""
