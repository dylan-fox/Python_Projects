#Study Drill
print "Here's what we've learned so far. \n"

#ex1
print "1: Sample printing \n"

#ex2
#Commenting

#ex3
print "3: Words and numbers, like", 5+5+28
print "Booleans, like", 54<57, "\n"

#ex4
#Setting variables
sample1 = 10
sample2 = 20
sampleMult = sample1 * sample2
print "4: Multiplying variables; %d and %d results in %d" %(sample1, sample2, sampleMult), "\n"

#ex5
#String formatting
print "5: You can use %s to represent strings, %d to represent ints, %f for floating points, and %r for anything."
print "You can also use round() to round numbers, like turning 53.25 into", round(53.25), "\n"

#ex6
#Working with strings
print "6: You can set variables to await a future value, such as patience = 'Waiting for this value: \%s'"
patience = "Waiting for this value: %s"
reward = "A string I named reward."
print patience % reward
print "You can also combine strings."
firstString = "Here's the left "
secondString = "and here's the right."
print firstString + secondString, "\n"

#ex7
#Combining strings
print "7: You can even multiply strings."
littleString = 'Wow! '
print littleString * 10, "\n"

#ex8
#More formatting
print "8: Some variables can be nothing but string formatters, waiting for input."
formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one", "two", "three", "four")
print formatter %(1<2, 5>6, 7<=21/3, "magic" == "magic"), "\n"

#ex9
#String formatting with line breaks and triple quotes
print "9: This is the exercise where we finally learn about the magical \nline break."
print """We also learn
That you can print on multiple lines
Using triple quotes after a print statement."""

#ex10
#Other string formatting
print """10: \t \\t gets you a horizontal tab.
\\\ gets you a \\.
\\' gets you a \'.
\\" gets you a \".
\\b backs up one space.
\\r backs you to the start of the line (a carraige return).
\\n gets you a new line.
\\f gets you a new page.
\\v gets you a \v vertical tab (in theory).
There were some other ones, but they weren't displaying in powershell.
"""

#ex11
#Raw input
print "11: Here's where we learn about raw_input(). Go ahead and enter something."
something = raw_input()
print "You entered %r." %something, "\n"

#ex12
#Raw input w/ prompt
print "12: Here we learned that entering something in raw_input's parenthesis makes a prompt."
something2 = raw_input("Enter something again.\n")
print "You entered %r." %something2, "\n"

#ex13
#Argument values from system.
print """13: Importing argument values from the system.
from sys import argv
script, first, second, third = argv
Now you have some values straight from the comand line to work with.
"""

#ex14
#Combining system inputs and raw inputs.
print "14: By combining system inputs and raw inputs, we can start with initial values and add more as we go.\n"

#ex15
#Importing and reading files from system
print """15: System values and raw input can also get you actual files.
Once you've imported a file, you can open it and set it to a variable.
Do that with the open() and read() methods, e.g.
    from sys import argv
    script, filename = argv
    txt = open(filename)
    print txt.read()
You can import a file with raw_input in a two step process just like importing via system.
    file_again = raw_input("> ")
    txt_again = open(file_again)
    print txt_again.read()
You can do this in the python shell via something like
    variable = open("ex15_sample.txt")
    print variable.read()
Wow! Files get tricky.
"""

#ex16
#Erasing and rewriting a file
print """16: Here's how to erase and write to files.
First, open it in write mode.
    from sys import argv
    script, filename = argv
    target = open(filename, 'w')
That will erase what's in the file, leaving you free to write in something new.
If it didn't do that, you could also use target.truncate().
Now you can write new stuff, and close to save.
    target.write(new_stuff)
    target.close()
You can do this in the python shell like so:
    opened_file = open("test.txt", "w")
    opened_file.write(new_stuff)
    opened_file.close()
See? Not so hard when you get used to it.
"""

#ex17
#Importing methods, verifying files, and copying files
print """17: Let's learn how to copy the contents of file 1 into file 2.
First, we open file 1 and assign to a variable, then assign its contents to a second variable.
    in_file = open(file1)
    indata = in_file.read()
We should confirm file 2 exists before we write to it. To do so, we import the 'exists' method from Python and run it on file 2.
    from os.path import exists
    print exists(file2)
Then, we open file 2 in write mode and write to it.
    out_file = open(file2, 'w')
    out_file.write(indata)
Finally, we close both files.
    in_file.close()
    out_file.close()
Done!
"""

#ex18
#Introduction to functions
print """18: Here we learn about functions.
A function looks like this:
    def some_function(*arguments):
        arg 1, arg2 = arguments
        #code
That one works like 'from sys import argv'. An easier way is:
    def some_function(arg1, arg2):
        #code
"""

#ex19
#More on functions
print """19: Functions can accept all kinds of arguments. Take this one:
    def some_function(a, b):
        print a + b
We can give it direct numbers:
    some_function(12, 523)
Or variables:
    firstval = 44
    secondval = 182
    some_function(firstval, secondval)
Or math:
    some_function(10+24, 2934/14*3)
Or even raw inputs:
    user_val_1 = int(raw_input("Enter the first value: "))
    user_val_2 = int(raw_input("Enter the second value: "))
    some_function(user_val_1, user_val_2)
"""

#ex20
#Manipulating files with functions
print """20: We can use functions on files, too.
For example:
    from sys import argv
    script, input_file = argv
    current_file = open(input_file)

    def print_all(f)
        print f.read()

    print_all(current_file)

We also learn about changing our position within a file and printing single lines in this exercise.
When you assign a file to a variable, python sets the position to be the 1st character of the 1st line.
Using a command like read() goes through the whole file, leaving you at the end.
In order to read it again, you have to set the position back to 0 with the seek method. For example:
    print current_file.read()
    current_file.seek(0)
Instead of reading the entire thing, you can also read only the current line.
    current_file.readline()
And of course, all of those can be included within functions.
"""

#ex21
#Functions that return
print """21: Functions can do more than just print or adjust files.
Many functions will return something based on their arguments.
That way, you can assign new variables as the result of functions. For example:
    def square_that_variable(a)
        return a*a

    to_be_squared = int(raw_input("What number do you want squared?"))
    result = square_that_variable(to_be_squared)
    print "Here you go! \%d" %result

And that's what we've learned so far.
"""
