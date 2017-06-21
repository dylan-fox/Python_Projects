#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""3. Mad Libs Generator

The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. The program
will first prompt the user for a series of inputs a la Mad Libs. For example, a
singular noun, an adjective, etc. Then, once all the information has been inputted,
the program will take that data and place them into a premade story template. You’ll
need prompts for user input, and to then print out the full story at the end with the
input included.
Concepts to keep in mind:
* Strings
* Variables
* Concatenation
* Print

A pretty fun beginning project that gets you thinking about how to manipulate
userinputted data. Compared to the prior projects, this project focuses far more
on strings and concatenating. Have some fun coming up with some wacky stories for
this!
"""

print "Let's play Mad Libs!"

adjective1 = raw_input("\nGive me an adjective. \n")
noun1 = raw_input("\nGive me a noun. \n")
noun2 = raw_input("\nGive me a noun. \n")
verb1 = raw_input("\nGive me a verb. \n")
noun3 = raw_input("\nGive me a noun. \n")
adverb1 = raw_input("\nGive me an adverb. \n")
verb2 = raw_input("\nGive me a verb, past tense. \n")
noun4 = raw_input("\nGive me a feeling. \n")

print "Okay, here we go!"

print """
One day, there was a %s %s. It really loved its %s, and would %s it every day.
But one day, a %s came along and %s %s its %s! The %s felt %s.
""" %(adjective1, noun1, noun2, verb1, noun3, adverb1, verb2, noun2, noun1, noun4)
