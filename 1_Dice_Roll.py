#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The Goal: Like the title suggests, this project involves writing a program that
simulates rolling dice. When the program runs, it will randomly choose a number
between 1 and 6. Or whatever other integer you prefer — the number of sides on
the die is up to you. The program will print what that number is. It should then
ask you if you’d like to roll again. For this project, you’ll need to set the min
and max number that your dice can produce. For the average die, that means a minimum
of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number
within that range and prints it.

Concepts to keep in mind:
* Random
* Integer
* Print
* While Loops

A good project for beginners, this project will help establish a solid foundation
for basic concepts. And if you already have programming experience, chances are that
the concepts used in this project aren’t completely foreign to you. Print, for example,
is similar to Javascript’s console.log."""

#Import Python's random number generator.
import random

#Welcome message.
print "Welcome to Dice Rolling simulator!"

#Get a string from the user.
dice_range = raw_input("Select a type of die to roll.\nd")

#Convert to an integer or throw an exception and ask for a new string.
while True:
    try:
        dice_range = int(dice_range)
        break
    except ValueError:
        dice_range = raw_input("Try a positive integer this time.\nd")

#Our dicerolling function.
def diceroll(dice_range):
    #Prompt the user for an integer dice size.
    #Check whether the number is positive.
    if dice_range > 0:
        #Roll the die!
        result =  random.randint(1, dice_range)
        print "You roll a %s" %result, "\n"
    else:
        print "Please enter a positive integer.\n"

#Initial roll.
diceroll(dice_range)

"""
#Repeat as long as user keeps entering 'y'.
repeat = True
while repeat == True:
    userprompt = raw_input("Would you like to roll again? y/n\n")
    if userprompt == "y":
        print "\n"
        diceroll()
    elif userprompt == "n":
        repeat = False
        print "Bye now!"
    else:
        repeat = False
        print "Not sure what that means. Bye now!"
"""

#Let's have it roll if given a number and exit otherwise.
#Need to rewrite above to have diceroll try the passed value.
while True:
    userprompt = raw_input("Enter an integer to roll that size die. \n")
    try:
        #int(userprompt)
        diceroll(int(userprompt))
    except ValueError:
        print "Bye now!\n"
        break
