#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The Goal: Similar to the first project, this project also uses the random module
in Python. The program will first randomly generate a number unknown to the user.
The user needs to guess what that number is. (In other words, the user needs to be
able to input information.) If the user’s guess is wrong, the program should return
some sort of indication as to how wrong (e.g. The number is too high or too low). If
the user guesses correctly, a positive indication should appear. You’ll need functions
to check if the user input is an actual number, to see the difference between the
inputted number and the randomly generated numbers, and to then compare the numbers.

Concepts to keep in mind:
* Random function
* Variables
* Integers
* Input/Output
* Print
* While loops
* If/Else statements


Jumping off the first project, this project continues to build up the base knowledge
and introduces user-inputted data at its very simplest. With user input, we start to
get into a little bit of variability."""

#Import Python's random module.
import random

#Takes a number as input, and generates a number between 1 and that.
from sys import argv
script, user_range = argv

#Function to compare a guess to the answer.
def compare(guess, answer):
    if guess < answer:
        print "You're too low! \n"
    elif guess > answer:
        print "You're too high! \n"
    elif guess == answer:
        print "You got it! \n"

#Generate a random number.
answer = random.randint(1, int(user_range))
print "I'm thinking of a number between 1 and %s. Can you guess what it is?\n" %user_range

while True:
    #Get a string from the user representing their guess.
    guess = raw_input("Pick a number. \n")

    #This will turn the user input into an integer, or else ask for a new one.
    while True:
        try:
            guess = int(guess)
            break
        except ValueError:
            guess = raw_input("Please enter an integer. \n")

    compare (guess, answer)
    if guess == answer:
        break
