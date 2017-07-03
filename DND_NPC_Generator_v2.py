#!/usr/bin/env python
# -*- coding: utf-8 -*-
#A program to generate random 5th edition NPCs.
import random

#First, we have the character class. Every character will be an instantiation of this class.
#Therefore, the class must remain a blank slate, but with functions to imbue objects with qualities.

class character:

    def __init__(self):
        """Set initial values for the character."""
        self.name = ''
        self.race = ''
        self.subrace = ''
        self.skills = []
        self.Str = 0
        self.Dex = 0
        self.Con = 0
        self.Int = 0
        self.Wis = 0
        self.Cha = 0
        self.level = 1
        self.profiency = 2
#---------------------------------------------------------------------------------------------------------------------
    def roll4d6(self):
        """Generates an ability score by rolling 4d6 and dropping the lowest."""
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)
        roll4 = random.randint(1,6)
        sortedRolls = sorted([roll1, roll2, roll3, roll4])
        return sortedRolls[1] + sortedRolls[2] + sortedRolls[3]
#---------------------------------------------------------------------------------------------------------------------
    def randomRace(self):
        """Assigns the character a random race and subrace."""
        #Generate a random number between 1 and 9, then reassign race based on that number.
        race = random.randint(1, 9)
        if race == 1:
            self.race = "Dragonborn"
            subrace = random.randint(1,10)
            if subrace == 1:
                self.subrace ="Black"
            elif subrace == 2:
                self.subrace ="Blue"
            elif subrace ==3:
                self.subrace ="Brass"
            elif subrace ==4:
                self.subrace = "Bronze"
            elif subrace ==5:
                self.subrace = "Copper"
            elif subrace ==6:
                self.subrace = "Gold"
            elif subrace == 7:
                self.subrace = "Green"
            elif subrace == 8:
                self.subrace = "Red"
            elif subrace == 9:
                self.subrace = "Silver"
            elif subrace == 10:
                self.subrace = "White"

        elif race == 2:
            self.race = "Dwarf"
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Hill"
            else:
                self.subrace = "Mountain"

        elif race == 3:
            self.race = "Elf"
            subrace = random.randint(1,5)
            if subrace == 1 or subrace == 2:
                self.subrace = "High"
            elif subrace == 3 or subrace == 4:
                self.subrace = "Wood"
            elif subrace == 5:
                self.subrace = "Drow"

        elif race == 4:
            self.race = "Gnome"
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Forest"
            elif subrace == 2:
                self.subrace = "Rock"

        elif race == 5:
            self.race = "Half-Elf"
            self.subrace = ""

        elif race == 6:
            self.race = "Half-Orc"
            self.subrace = ""

        elif race == 7:
            self.race = "Halfling"
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Lightfoot"
            elif subrace == 2:
                self.subrace = "Stout"

        elif race == 8:
            self.race = "Human"
            self.subrace = ""

        elif race == 9:
            self.race = "Tiefling"
            self.subrace = ""
#---------------------------------------------------------------------------------------------------------------------
    def randomSubRace(self):
        """Assigns a random subrace."""
        if self.race == 'Dragonborn':
            subrace = random.randint(1,10)
            if subrace == 1:
                self.subrace ="Black"
            elif subrace == 2:
                self.subrace ="Blue"
            elif subrace ==3:
                self.subrace ="Brass"
            elif subrace ==4:
                self.subrace = "Bronze"
            elif subrace ==5:
                self.subrace = "Copper"
            elif subrace ==6:
                self.subrace = "Gold"
            elif subrace == 7:
                self.subrace = "Green"
            elif subrace == 8:
                self.subrace = "Red"
            elif subrace == 9:
                self.subrace = "Silver"
            elif subrace == 10:
                self.subrace = "White"

        elif self.race == 'Dwarf':
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Hill"
            else:
                self.subrace = "Mountain"

        elif self.race == 'Elf':
            subrace = random.randint(1,5)
            if subrace == 1 or subrace == 2:
                self.subrace = "High"
            elif subrace == 3 or subrace == 4:
                self.subrace = "Wood"
            elif subrace == 5:
                self.subrace = "Drow"

        elif self.race == 'Gnome':
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Forest"
            elif subrace == 2:
                self.subrace = "Rock"

        elif self.race == 'Halfling':
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Lightfoot"
            elif subrace == 2:
                self.subrace = "Stout"

        else:
            self.subrace = ''
#---------------------------------------------------------------------------------------------------------------------
    def charDescription(self):
        """Returns the description of the character."""
        charDescription = "%s is a level %d %s %s. \nSkills: %s" %(self.name, self.level, self.subrace, self.race, ", ".join(sorted(self.skills)))
        return charDescription
#---------------------------------------------------------------------------------------------------------------------

Robin = character()
Robin.name = 'Robin'
Robin.race = 'Halfling'
Robin.subrace = 'Lightfoot'
Robin.skills = ['Stealth', 'Sleight of Hand', 'Arcana']
print Robin.charDescription()
Robin.Str = Robin.roll4d6()
print Robin.Str
print Robin.Dex
print ""

Stranger = character()
Stranger.name = "Stranger"
Stranger.randomRace()
print Stranger.charDescription()
print "And now, a change of subrace."
Stranger.randomSubRace()
print Stranger.charDescription()

"""
StrangeDwarf = character()
StrangeDwarf.name = "StrangeDwarf"
StrangeDwarf.race = 'Dwarf'
StrangeDwarf.subrace = 'Hill'
print StrangeDwarf.charDescription()
print ""

StrangeDragonBorn = character()
StrangeDragonBorn.name = 'Strange Dragonborn'
StrangeDragonBorn.race = 'Dragonborn'
StrangeDragonBorn.randomSubRace()
print StrangeDragonBorn.charDescription()
StrangeDragonBorn.randomSubRace()
print StrangeDragonBorn.charDescription()
StrangeDragonBorn.randomSubRace()
print StrangeDragonBorn.charDescription()
"""
