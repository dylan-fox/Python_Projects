from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

'''
from sys import argv

script, one = argv

print "So, the first argument value is the script name, namely", script
print "And then anything you pass after the script, like", one, ", come later"
'''

"""
from sys import argv

one, script = argv

print "But can you put the script afterward? The script this time is", script
print "And the variable is", one
"""
#nope, that doesn't work. Script name has to be the first item you enter after 'python'

"""
from sys import argv

script, a, b, c, d, e, f, g = argv

print "This time the name of the script is", script
print "And the variables are: \n", a, "\n", b, "\n", c, "\n", d, "\n", e, "\n", f, "\n", g
print "Using pluses you get:" + a + b + c + d + e + f + g
#so commas add spaces, and pluses don't. good to know
"""

userinfo = raw_input("Would you like to add a variable?\n")
print "Sure, the newest variable on the crew is \""+ userinfo + "\""
#remember to add that space or line break after the prompt in raw input
