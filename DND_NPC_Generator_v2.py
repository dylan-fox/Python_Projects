#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A program to generate random 5th edition NPCs.

The goal is to be able to create a batch of random characters.
Given certain parameters (e.g. male outlander dwarf sorcerer) it should be able
to create a batch following those parameters.

First, we have the character class. Every character will be an instantiation of this class.
Therefore, the class must remain a blank slate, but with functions to imbue objects with qualities.

Then, we can write functions that create an object of that class, imbue them with specific qualities,
and issue the remaining qualities at random.

Now, should we make the backgrounds, races, and classes inherited classes?
Such that when a class takes on one of those attributes, it brings a number of other
attributes with it?

If we have a Fighter, they should have attributes such as Fighting Style and Martial Archetype.
If we have a Dwarf, they should have attributes such as subrace. It should also alter name, scores, proficiencies, and more.

Seems like every race, background, and class affects the character and brings new things to the table. We should start
with an initial character, then adjust the values based on race, background, and class. Those will all inherit character's
attributes and methods.

So should we have a Race class inherit Character, and then a Dwarf class inherit Race? What is common across all
races, backgrounds, and classes?
-Races grant ability score increases, names, age, size, speed, proficiencies, and other abilities.
-Backgrounds grant proficiencies, equipment, and a feature.
-Classes grant hp, proficiencies, saving throws, and abilities.
So we could make race, background, and class superclasses with methods for adjusting ability scores, etc.
Or we could define those for Character and then simply have the other attributes exist as their own classes.

But let's say we want a dwarf fighter. We can call up a Dwarf object that has ability scores, etc. from Character.
The Dwarf could then call upon its Race methods to set e.g. a name. But then what? I can't call Fighter for the same object
since it's a different class than Dwarf.

I think we're best off writing methods that adjust profiencies, etc. based on existing parameters.
We should be able to summon a character with certain attributes, and if those aren't given then set them at random.
"""
import random

class character:

#    def __init__(self, race = None, background = None, charClass = None, gender = None):
    def __init__(self, **charInfo):
        """Set initial values for the character."""

        #Race
        if charInfo.setdefault('race', None) == None:
            self.randomRace()
        else:
            self.race = charInfo['race']
            self.randomSubRace()

        #Background
        if charInfo.setdefault('background', None) == None:
            self.randomBackground()
        else:
            self.background = charInfo['background']

        #Class
        if charInfo.setdefault('charClass', None) == None:
            self.randomClass()
        else:
            self.charClass = charInfo['charClass']

        #Gender
        if charInfo.setdefault('gender', None) == None:
            gender = random.randint(1,2)
            if gender == 1:
                self.gender = 'male'
            else:
                self.gender = 'female'
        else:
            self.gender = charInfo['gender']

        #Name
        self.randomName(self.race, self.gender)

        #Proficiencies
        self.proficiencies = []
        self.setProficiencies()
        #This will reroll skills until no duplicates are detected.
        while len(self.proficiencies) > len(set(self.proficiencies)):
            self.proficiencies = []
            #print 'Duplicates found, trying again.'
            self.setProficiencies()
            #print 'New proficiencies:', sorted(self.proficiencies)

        #Attributes
        self.attributes = {
            'Str': 0,
            'Dex': 0,
            'Con': 0,
            'Int': 0,
            'Wis': 0,
            'Cha': 0
        }
        self.setAttributes()

        #Level
        self.level = 1

        #Proficiency Bonus
        self.profBonus = 2

        #Adjectives
        self.adjectives = []
        self.setAdjectives()

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Key Character Functions
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
            self.subrace = None

        elif race == 6:
            self.race = "Half-Orc"
            self.subrace = None

        elif race == 7:
            self.race = "Halfling"
            subrace = random.randint(1,2)
            if subrace == 1:
                self.subrace = "Lightfoot"
            elif subrace == 2:
                self.subrace = "Stout"

        elif race == 8:
            self.race = "Human"
            self.subrace = None

        elif race == 9:
            self.race = "Tiefling"
            self.subrace = None
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
            self.subrace = None
#---------------------------------------------------------------------------------------------------------------------
    def randomBackground(self):
        """Assigns the character a random background."""
        background = random.randint(1, 13)
        if background == 1:
            self.background = "Acolyte"
        elif background == 2:
            self.background = "Charlatan"
        elif background == 3:
            self.background = "Criminal"
        elif background == 4:
            self.background = "Entertainer"
        elif background == 5:
            self.background = "Folk Hero"
        elif background == 6:
            self.background = "Guild Artisan"
        elif background == 7:
            self.background = "Hermit"
        elif background == 8:
            self.background = "Noble"
        elif background == 9:
            self.background = "Outlander"
        elif background == 10:
            self.background = "Sage"
        elif background == 11:
            self.background = "Sailor"
        elif background == 12:
            self.background = "Soldier"
        elif background == 13:
            self.background = "Urchin"
#---------------------------------------------------------------------------------------------------------------------
    def randomClass(self):
        """Assigns the character a random class."""
        charClass = random.randint(1, 12)
        if charClass == 1:
            self.charClass = "Barbarian"
        elif charClass == 2:
            self.charClass = "Bard"
        elif charClass == 3:
            self.charClass = "Cleric"
        elif charClass == 4:
            self.charClass = "Druid"
        elif charClass == 5:
            self.charClass = "Fighter"
        elif charClass == 6:
            self.charClass = "Monk"
        elif charClass == 7:
            self.charClass = "Paladin"
        elif charClass == 8:
            self.charClass = "Ranger"
        elif charClass == 9:
            self.charClass = "Rogue"
        elif charClass == 10:
            self.charClass = "Sorcerer"
        elif charClass == 11:
            self.charClass = "Warlock"
        elif charClass == 12:
            self.charClass = "Wizard"
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Attribute Functions
    def roll4d6(self):
        """Generates an ability score by rolling 4d6 and dropping the lowest."""
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)
        roll4 = random.randint(1,6)
        sortedRolls = sorted([roll1, roll2, roll3, roll4])
        return sortedRolls[1] + sortedRolls[2] + sortedRolls[3]
#---------------------------------------------------------------------------------------------------------------------
    def setAttributes(self):
        """Sets attributes based on class and race."""
        #First, roll 4d6 and sort from lowest to highest.
        scores = sorted([self.roll4d6(), self.roll4d6(), self.roll4d6(), self.roll4d6(), self.roll4d6(), self.roll4d6()])
        #print sortedScores

        #Set a random number for later use.
        rand = random.randint(1,6)

        #Next, based on class, assign the highest two scores to a primary and secondary attribute, then the rest at random.
        primary = scores.pop()
        secondary = scores.pop()
        random.shuffle(scores)

        if self.charClass == 'Barbarian':
            self.attributes['Str'] = primary
            self.attributes['Con'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Bard':
            self.attributes['Cha'] = primary
            if rand <=3:
                self.attributes['Str'] = secondary
            else:
                self.attributes['Dex'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Cleric':
            self.attributes['Wis'] = primary
            if rand <=3:
                self.attributes['Str'] = secondary
            else:
                self.attributes['Dex'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Druid':
            self.attributes['Wis'] = primary
            if rand <=3:
                self.attributes['Str'] = secondary
            else:
                self.attributes['Dex'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Fighter':
            if rand <=3:
                self.attributes['Str'] = primary
            else:
                self.attributes['Dex'] = primary
            self.attributes['Con'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Monk':
            if rand <=3:
                self.attributes['Str'] = primary
            else:
                self.attributes['Dex'] = primary
            self.attributes['Wis'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Paladin':
            if rand <=3:
                self.attributes['Str'] = primary
            else:
                self.attributes['Dex'] = primary
            self.attributes['Cha'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Ranger':
            #Primary: charisma, secondary: Str or Dex
            if rand <=3:
                self.attributes['Str'] = primary
            else:
                self.attributes['Dex'] = primary
            self.attributes['Wis'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Rogue':
            self.attributes['Dex'] = primary
            if rand <=3:
                self.attributes['Int'] = secondary
            else:
                self.attributes['Cha'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Sorcerer':
            self.attributes['Cha'] = primary
            if rand <=3:
                self.attributes['Dex'] = secondary
            else:
                self.attributes['Con'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Warlock':
            self.attributes['Cha'] = primary
            if rand <=3:
                self.attributes['Dex'] = secondary
            else:
                self.attributes['Con'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()

        elif self.charClass == 'Wizard':
            self.attributes['Int'] = primary
            if rand <=3:
                self.attributes['Dex'] = secondary
            else:
                self.attributes['Con'] = secondary
            for att, score in self.attributes.iteritems():
                if score == 0:
                    self.attributes[att] = scores.pop()


        #Next, assign bonuses based on race and subrace.
        if self.race == "Dragonborn":
            self.attributes['Str'] +=2
            self.attributes['Cha'] +=1
        elif self.race == "Dwarf":
            if self.subrace == "Hill":
                self.attributes['Wis'] +=1
            elif self.subrace == "Mountain":
                self.attributes['Str'] +=2
        elif self.race == "Elf":
            self.attributes['Dex'] +=2
            if self.subrace == "High":
                self.attributes['Int'] +=1
            elif self.subrace == "Wood":
                self.attributes['Wis'] +=1
            elif self.subrace == "Drow":
                self.attributes['Cha'] +=1
        elif self.race == "Gnome":
            self.attributes['Int'] +=2
            if self.subrace == "Forest":
                self.attributes['Dex'] +=1
            elif self.subrace == "Rock":
                self.attributes['Con'] +=1
        elif self.race == "Half-Elf":
            self.attributes['Cha'] +=2
            #print "Stats before boost: %i %i %i %i %i %i" %(Str, Dex, Con, Int, Wis, Cha)
            raceBoost = random.sample([1, 2, 3, 4, 5], 2)
            if raceBoost[0] == 1 or raceBoost[1] == 1:
                self.attributes['Str'] +=1
                #print "Boosted Str"
            if raceBoost[0] == 2 or raceBoost[1] == 2:
                self.attributes['Dex'] +=1
               #print "Boosted Dex"
            if raceBoost[0] == 3 or raceBoost[1] == 3:
                self.attributes['Con'] +=1
                #print "Boosted Con"
            if raceBoost[0] == 4 or raceBoost[1] == 4:
                self.attributes['Int'] +=1
                #print "Boosted Int"
            if raceBoost[0] == 5 or raceBoost[1] == 5:
                self.attributes['Wis'] +=1
                #print "Boosted Wis"
            #print "Stats after boost: %i %i %i %i %i %i" %(Str, Dex, Con, Int, Wis, Cha)

        elif self.race == "Half-Orc":
            self.attributes['Str'] +=2
            self.attributes['Con'] +=1

        elif self.race == "Halfling":
            self.attributes['Dex'] +=2
            if self.subrace == "Lightfoot":
                self.attributes['Cha'] +=1
            elif self.subrace == "Stout":
                self.attributes['Con'] +=1

        elif self.race == "Human":
            raceBoost = random.sample([1, 2, 3, 4, 5, 6], 2)
            if raceBoost[0] == 1 or raceBoost[1] == 1:
                self.attributes['Str'] +=1
                #print "Boosted Str"
            if raceBoost[0] == 2 or raceBoost[1] == 2:
                self.attributes['Dex'] +=1
                #print "Boosted Dex"
            if raceBoost[0] == 3 or raceBoost[1] == 3:
                self.attributes['Con'] +=1
                #print "Boosted Con"
            if raceBoost[0] == 4 or raceBoost[1] == 4:
                self.attributes['Int'] +=1
                #print "Boosted Int"
            if raceBoost[0] == 5 or raceBoost[1] == 5:
                self.attributes['Wis'] +=1
               #print "Boosted Wis"
            if raceBoost[0] == 6 or raceBoost[1] == 6:
                self.attributes['Cha'] +=1
                #print "Boosted Cha"

        elif self.race == "Tiefling":
            self.attributes['Int'] +=1
            self.attributes['Cha'] +=2
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Proficiency Functions
    def randomProficiencies(self, quantity):
        """Returns a given number of random skills."""
        skillRange = range(1,19)
        bonusSkills = random.sample(skillRange, quantity)
        skills = []
        if 1 in bonusSkills:
            skills.append("Athletics")
            # += ["Athletics"]
        if 2 in bonusSkills:
            skills += ["Acrobatics"]
        if 3 in bonusSkills:
            skills += ["Sleight of Hand"]
        if 4 in bonusSkills:
            skills += ["Stealth"]
        if 5 in bonusSkills:
            skills += ["Arcana"]
        if 6 in bonusSkills:
            skills += ["History"]
        if 7 in bonusSkills:
            skills += ["Investigation"]
        if 8 in bonusSkills:
            skills += ["Nature"]
        if 9 in bonusSkills:
            skills += ["Religion"]
        if 10 in bonusSkills:
            skills += ["Animal Handling"]
        if 11 in bonusSkills:
            skills += ["Insight"]
        if 12 in bonusSkills:
            skills += ["Medicine"]
        if 13 in bonusSkills:
            skills += ["Perception"]
        if 14 in bonusSkills:
            skills += ["Survival"]
        if 15 in bonusSkills:
            skills += ["Deception"]
        if 16 in bonusSkills:
            skills += ["Intimidation"]
        if 17 in bonusSkills:
            skills += ["Performance"]
        if 18 in bonusSkills:
            skills += ["Persuasion"]
        return skills
#---------------------------------------------------------------------------------------------------------------------
    def setProficiencies(self):
        """Assign proficiencies based on race, background, and class."""

        #races
        if self.race == "Dwarf":
            self.proficiencies +=["Artisan's tools"]
        elif self.race == "Half-Orc":
            self.proficiencies +=["Intimidate"]
        elif self.race == "Elf":
            self.proficiencies += ["Perception"]
        elif self.race == "Gnome" and self.subrace == "Rock":
            self.proficiencies += ["Tinker's tools"]
        elif self.race == "Half-Elf":
            self.proficiencies += self.randomProficiencies(2)
        elif self.race == "Half-Orc":
            self.proficiencies += ["Intimidate"]
        elif self.race == "Human":
            self.proficiencies += self.randomProficiencies(1)

        #backgrounds
        if self.background == "Acolyte":
            self.proficiencies +=["Insight", "Religion"]
        if self.background == "Charlatan":
            self.proficiencies +=["Deception", "Sleight of Hand", "Disguise Kit", "Forgery Kit"]
        if self.background == "Criminal":
            self.proficiencies +=["Deception", "Stealth", "Gaming Set", "Thieves' Tools"]
        if self.background == "Entertainer":
            self.proficiencies +=["Acrobatics", "Performance", "Musical Instrument", "Disguise Kit"]
        if self.background == "Folk Hero":
            self.proficiencies +=["Animal Handling", "Survival", "Artisan's Tools", "Land Vehicles"]
        if self.background == "Guild Artisan":
            self.proficiencies +=["Insight", "Persuasion", "Artisan's Tools"]
        if self.background == "Hermit":
            self.proficiencies +=["Medicine", "Religion", "Herbalism Kit"]
        if self.background == "Noble":
            self.proficiencies +=["History", "Persuasion", "Gaming Set"]
        if self.background == "Outlander":
            self.proficiencies +=["Athletics", "Survival", "Musical Instrument"]
        if self.background == "Sage":
            self.proficiencies +=["Arcana", "History"]
        if self.background == "Sailor":
            self.proficiencies +=["Athletics", "Perception", "Navigator's Tools", "Water Vehicles"]
        if self.background == "Soldier":
            self.proficiencies +=["Athletics", "Intimidation", "Gaming Set", "Land Vehicles"]
        if self.background == "Urchin":
            self.proficiencies +=["Sleight of Hand", "Stealth", "Disguise Kit", "Thieves' Tools"]

        #classes
        if self.charClass == "Barbarian":
            newProficiencies = random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Bard":
            self.proficiencies += self.randomProficiencies(3)
        elif self.charClass == "Cleric":
            newProficiencies = random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Druid":
            newProficiencies = random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Fighter":
            newProficiencies = random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Monk":
            newProficiencies = random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Paladin":
            newProficiencies = random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Ranger":
            newProficiencies = random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1], newProficiencies[2]]
        elif self.charClass == "Rogue":
            newProficiencies = random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1], newProficiencies[2], newProficiencies[3]]
        elif self.charClass == "Sorcerer":
            newProficiencies = random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Warlock":
            newProficiencies = random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]
        elif self.charClass == "Wizard":
            newProficiencies = random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2)
            self.proficiencies +=[newProficiencies[0], newProficiencies[1]]

        """This way replaces duplicate proficiencies with random ones. It may
        be slightly faster, but it also distributes proficiencies that characters
        have no ways of getting.

        #Replace duplicates with random proficiencies
        #While loop checks that the length of the unique skill list = length of skill list
        #print len(self.proficiencies), len(set(self.proficiencies))
        while len(self.proficiencies) > len(set(self.proficiencies)):
            #print 'Proficiencies:', self.proficiencies
            enProf = list(enumerate(self.proficiencies))
            #print 'enProf:', enProf
            duplicate = False
            for testIndex, tested in enProf:
                #print 'test:', testIndex, tested
                #compare x against other elements of proficiencies
                for comparisonIndex, comparison in enProf:
                    #print 'comparison:', comparisonIndex, comparison
                    if tested == comparison and testIndex != comparisonIndex:
                        #print 'Duplicate found'
                        duplicate = True
                        duplicateIndex = testIndex
                        break
                if duplicate == True:
                    break

            #If a duplicate was detected, change the tested proficiency
            if duplicate == True:
                newProf = self.randomProficiencies(1)
                self.proficiencies[duplicateIndex] = newProf[0]
                #print 'replaced %s with %s' %(tested, self.proficiencies[duplicateIndex])
                #print 'Proficiencies:', self.proficiencies
        """

        #sort list
        self.proficiencies = sorted(self.proficiencies)

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Descriptor Functions
    def randomName(self, race, gender):
        """Sets name based on race and gender."""
        if race == 'Dwarf':
            maleFirstNameRange = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor',
                'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil', 'Fargrim',
                'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik',
                'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin', 'Torin',
                'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit', 'Vondalh']
            femaleFirstNameRange = ['Amber', 'Artin', 'Audhild', 'Bardryn',
                'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda',
                'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 'Liftrasa',
                'Mardred', 'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra']
            lastNameRange = ['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil',
                'Fireforge', 'Frostbeard', 'Gorunn', 'Holderhek', 'Ironfist', 'Loderr',
                'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart']
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Elf':
            maleFirstNameRange = ['Adran', 'Aelar', 'Aramil', 'Arannis',
                'Aust', 'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan',
                'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios',
                'Laucian', 'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon',
                'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis']
            femaleFirstNameRange = """Adrie, Althaea, Anastrianna, Andraste, Antinua, Bethrynna, Birel, Caelynn, Drusilia, Enna, Felosial, Ielenia, Jelenneth, Keyleth, Leshanna, Lia, Meriele, Mialee, Naivara, Quelenna, Quillathe, Sariel, Shanairra, Shava, Silaqui, Theirastra, Thia, Vadania, Valanthe, Xanaphia""".split(", ")
            lastNameRange = """Amakiir, Amastacia, Galanodel, Holimion, Ilphelkiir, Liadon, Meliamne, Nai'lo, Siannodel, Xiloscient""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Halfling':
            maleFirstNameRange = '''Alton, Ander, Cade, Corrin, Eldon, Errich, Finnan, Garret, Lindal, Lyle, Merric, Milo, Osborn, Perrin, Reed, Roscoe, Wellby'''.split(', ')
            femaleFirstNameRange = """Andry, Bree, Callie, Cora, Euphemia, Jillian, Kithri, Lavinia, Lidda, Merla, Nedda, Paela, Portia, Seraphina, Shaena, Trym, Vani, Verna""".split(", ")
            lastNameRange = """Brushgather, Goodbarrel, Greenbottle, High-hill, Hilltopple, Leagallow, Tealeaf, Thorngage, Tosscobble, Underbough""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Human':
            ethnicity = random.randint(1,9)
            if ethnicity == 1: #Calishite
                maleFirstNameRange = """Aseir, Bardeid, Haseid, Khemed, Mehmen, Sudeiman, Zasheir""".split(', ')
                femaleFirstNameRange = """Atala, Ceidil, Hama, Jasmal, Meilil, Seipora, Yasheira, Zasheida""".split(", ")
                lastNameRange = """Basha, Dumein, Jassan, Khalid, Mostana, Pashar, Rein""".split(", ")
            elif ethnicity == 2: #Chondathan
                maleFirstNameRange = """Darvin, Dorn, Evendur, Gorstag, Grim, Helm, Malark, Morn, Randal, Stedd""".split(', ')
                femaleFirstNameRange = """Arveene, Esvele, Jhessail, Kerri, Lureene, Miri, Rowan, Shandri, Tessele""".split(", ")
                lastNameRange = """Amblecrown, Buckman, Dundragon, Evenwood, Greycastle, Tallstag""".split(", ")
            elif ethnicity == 3: #Damaran
                maleFirstNameRange = """Bor, Fodel, Glar, Grigor, Igan, Ivor, Kosef, Mival, Orel, Pavel, Sergor""".split(', ')
                femaleFirstNameRange = """Alethra, Kara, Katernin, Mara, Natali, Olma, Tana, Zora""".split(", ")
                lastNameRange = """Bersk, Chernin, Dotsk, Kulenov, Marsk, Nemetsk, Shemov, Starag""".split(", ")
            elif ethnicity == 4: #Illuskan
                maleFirstNameRange = """Ander, Blath, Bran, Frath, Geth, Lander, Luth, Malcer, Stor, Taman, Urth""".split(', ')
                femaleFirstNameRange = """Amafrey, Betha, Cefrey, Kethra, Mara, Olga, Silifrey, Westra""".split(", ")
                lastNameRange = """Brightwood, Helder, Hornraven, Lackman, Stormwind, Windrivver""".split(", ")
            elif ethnicity == 5: #Mulan
                maleFirstNameRange = """Aoth, Bareris, Ehput-Ki, Kethoth, Mumed, Ramas, So-Kehur, Thazar-De, Urhur""".split(', ')
                femaleFirstNameRange = """Arizima, Chathi, Nephis, Nulara, Murithi, Sefris, Thola, Umara, Zolis""".split(", ")
                lastNameRange = """Ankhalab, Anskuld, Fezim, Hahpet, Nathandem, Sepret, Uuthrakt""".split(", ")
            elif ethnicity == 6: #Rashemi
                maleFirstNameRange = """Borivik, Faurgar, Jandar, Kanithar, Madislak, Ralmevik, Shaumar, Vladislak""".split(', ')
                femaleFirstNameRange = """Fyevarra, Hulmarra, Immith, Imzel, Navarra, Shevarra, Tammith. Yuldra""".split(", ")
                lastNameRange = """Chergoba, Dyernina, Iltazyara, Murnyethara, Stayanoga, Ulmokina""".split(", ")
            elif ethnicity == 7: #Shou
                maleFirstNameRange = """An, Chen, Chi, Fai, Jiang, Jun, Lian, Long, Meng, On, Shan, Shui, Wen""".split(', ')
                femaleFirstNameRange = """Bai, Chao, Jia, Lei, Mei, Qiao, Shui, Tai""".split(", ")
                lastNameRange = """Chien, Huang, Kao, Kung, Lao, Ling, Mei, Pin, Shin, Sum, Tan, Wan""".split(", ")
            elif ethnicity == 8: #Tethyrian
                maleFirstNameRange = """Darvin, Dorn, Evendur, Gorstag, Grim, Helm, Malark, Morn, Randal, Stedd""".split(', ')
                femaleFirstNameRange = """Arveene, Esvele, Jhessail, Kerri, Lureene, Miri, Rowan, Shandri, Tessele""".split(", ")
                lastNameRange = """Amblecrown, Buckman, Dundragon, Evenwood, Greycastle, Tallstag""".split(", ")
            elif ethnicity == 9: #Turami
                maleFirstNameRange = """Anton, Diero, Marcon, Pieron, Rimardo, Romero, Salazar, Umbero""".split(', ')
                femaleFirstNameRange = """Balama, Dona, Faila, Jalana, Luisa, Marta, Quara, Selise, Vonda""".split(", ")
                lastNameRange = """Agosto, Astorio, Calabra, Domine, Falone, Marivaldi, Pisacar, Ramondo""".split(", ")

            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Dragonborn':
            maleFirstNameRange = '''Arjhan, Balasar, Bharash, Donaar, Ghesh, Heskan, Kriv, Medrash, Mehen, Nadarr, Pandjed, Patrin, Rhogar, Shamash, Shedinn, Tarhun, Torinn'''.split(', ')
            femaleFirstNameRange = """Akra, Biri, Daar, Farideh, Harann, Flavilar, Jheri, Kava, Korinn, Mishann, Nala, Perra, Raiann, Sora, Surina, Thava, Uadjit""".split(", ")
            lastNameRange = """Clethtinthiallor, Daardendrian, Delmirev, Drachedandion, Fenkenkabradon, Kepeshkmolik, Kerrhylon, Kimbatuul, Linxakasendalor, Myastan, Nemmonis, Norixius, Ophinshtalajiir, Prexijandilin, Shestendeliath, Turnuroth, Verthisathurgiesh, Yarjerit""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Gnome':
            maleFirstNameRange = '''Alston, Alvyn, Boddynock, Brocc, Burgell, Dimble, Eldon, Erky, Fonkin, Frug, Gerbo, Gimble, Glim, Jebeddo, Kellen, Namfoodle, Orryn, Roondar, Seebo, Sindri, Warryn, Wrenn, Zook'''.split(', ')
            femaleFirstNameRange = """Bimpnottin, Breena, Caramip, Carlin, Donella, Duvamil, Ella, Ellyjobell, Ellywick, Lilli, Loopmottin, Lorilla, Mardnab, Nissa, Nyx, Oda, Orla, Roywyn, Shamil, Tana, Waywocket, Zanna""".split(", ")
            lastNameRange = """Beren, Daergel, Folkor, Garrick, Nackle, Murnig, Ningel, Raulnor, Scheppen, Timbers, Turen""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Half-Elf':
            maleFirstNameRange = ['Adran', 'Aelar', 'Aramil', 'Arannis',
                'Aust', 'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 'Erevan',
                'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios',
                'Laucian', 'Mindartis', 'Paelias', 'Peren', 'Quarion', 'Riardon',
                'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis']
            femaleFirstNameRange = """Adrie, Althaea, Anastrianna, Andraste, Antinua, Bethrynna, Birel, Caelynn, Drusilia, Enna, Felosial, Ielenia, Jelenneth, Keyleth, Leshanna, Lia, Meriele, Mialee, Naivara, Quelenna, Quillathe, Sariel, Shanairra, Shava, Silaqui, Theirastra, Thia, Vadania, Valanthe, Xanaphia""".split(", ")
            lastNameRange = """Amakiir, Amastacia, Galanodel, Holimion, Ilphelkiir, Liadon, Meliamne, Nai'lo, Siannodel, Xiloscient""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        elif race == 'Half-Orc':
            maleFirstNameRange = '''Dench, Feng, Gell, Henk, Holg, Imsh, Keth, Krusk, Mhurren, Ront, Shump, Thokk'''.split(', ')
            femaleFirstNameRange = """Baggi, Emen, Engong, Kansif, Myev, Neega, Ovak, Ownka, Shautha, Sutha, Vola, Volen, Yevelda""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            self.name = firstName

        elif race == 'Tiefling':
            maleFirstNameRange = '''Akmenos, Amnon, Barakas, Damakos, Ekemon, Iados, Kairon, Leucis, Melech, Mordai, Morthos, Pelaios, Skamos, Therai'''.split(', ')
            femaleFirstNameRange = """Akta, Anakis, Bryseis, Criella, Damaia, Ea, Kallista, Lerissa, Makaria, Nemeia, Orianna, Phelaia, Rieta""".split(", ")
            lastNameRange = """Art, Carrion, Chant, Creed, Despair, Excellence, Fear, Glory, Hope, Ideal, Music, Nowhere, Open, Poetry, Quest, Random, Reverence, Sorrow, Temerity, Torment, Weary""".split(", ")
            if gender == 'male':
                firstName = str(random.choice(maleFirstNameRange))
            else:
                firstName = str(random.choice(femaleFirstNameRange))
            lastName = str(random.choice(lastNameRange))
            self.name = "%s %s" %(firstName, lastName)

        else:
            self.name = 'SampleName'
#---------------------------------------------------------------------------------------------------------------------
    def setAdjectives(self):
        """Generates a list of 3 random adjectives to describe the character."""
        #Set a list of adjectives.
        allAdjectives ="""absurd, adorable, aged, amazing, ancient, animated, annoying, arrogant, attractive, awesome, awful, awkward, bashful, beautiful, believable, big, bitter, boisterous, bold, boring, brave, bright, brilliant, brutal, busy, calm, careful, caring, casual, charming, cheerful, cheesy, chubby, clean, clear, clever, clueless, clumsy, cold, colorful, comical, conceited, confused, confusing, cool, corrupt, cosmopolitan, courageous, cowardly, cranky, crazy, creative, creepy, crisp, cruel, cuddly, curvy, cute, dainty, daring, dark, dashing, deadly, delicate, delightful, demanding, depressing, desperate, devious, dignified, dirty, disgusting, distinguished, disturbing, dramatic, dreamy, dull, dumb, dysfunctional, earthy, eccentric, edgy, elderly, elitist, emotional, enchanting, energetic, enormous, entertaining, excitable, explosive, exquisite, fabulous, famous, fancy, fashionable, fast, fat, fearful, feminine, filthy, flaky, flamboyant, flat, fragrant, frail, frazzled, fresh, friendly, frightening, funky, funny, furious, furry, fuzzy, gentle, gigantic, glamorous, glitzy, gloomy, glorious, goofy, gorgeous, graceful, grueling, gruesome, grungy, hairy, handsome, happy, hardworking, harsh, haunting, healthy, heavy, helpful, hilarious, honest, honorable, horrifying, hostile, hot, humorous, idiotic, industrious, influential, innocent, insane, intense, irresistable, irrirtating, jolly, kind, lazy, legendary, little, lively, loud, lovable, lucky, lumpy, luscious, manly, masculine, mean, meek, melodramatic, mesmerizing, messy, mischievous, miserable, misunderstood, modern, mysterious, mystical, naive, nasty, neat, naughty, nerdy, nice, noisy, normal, nutty, obnoxious, obscene, odd, offensive, old, orderly, ordinary, outrageous, pale, pathetic, patriotic, peaceful, perverse, philosophical, phony, plain, playful, pleasant, polite, poor, popular, powerful, practical, pretty, primitive, principled, profound, proud, puffy, pure, quick, quiet, radical, realistic, refined, relaxed, repulsive, respectable, responsible, revolutionary, rich, ridiculous, risky, rough, round, sad, saintly, sappy, scary, secretive, selfish, senseless, sensitive, sensual, serious, sexy, shaggy, shallow, sharp, short, shy, silent, silly, simple, skillful, skinny, slender, slimy, slippery, sloppy, slow, sluggish, small, smart, smooth, snappy, sneaky, soft, sophisticated, sour, speedy, spiritual, spooky, spunky, sticky, stinky, strange, strong, stunning, stupid, sultry, surprising, sweet, swift, talented, tall, tame, temperamental, tender, terrible, terrific, thick, thin, thoughtful, tiny, timeless, tormented, tough, trashy, trustworthy, twisted, ugly, unbelievable, unforgettable, unhappy, unhealthy, unscrupulous, unusual, untamed, vain, violent, virtuous, visionary, warm, weak, weird, whimsical, wicked, wild, wired, witty, woebegone, wonderful, worldly, young, zany,
        """.split(', ')
        #Sample from them at random.
        self.adjectives += random.sample(allAdjectives, 3)
        f = self.adjectives[0][0]
        if f == 'a' or f == 'e' or f == 'i' or f == 'o' or f == 'u':
            self.shouldAn = "n"
        else:
            self.shouldAn = ""

#    def setAppearance(self):
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """Returns the description of the character."""
        #Core descriptors (name, gender, level, race, background, class)

        #check if subrace exists
        if self.subrace == None:
            subPrint = " "
        else:
            subPrint = " " + self.subrace + " "

        coreString = "%s is a%s %s, %s, %s %s%s%s %s %s." %(self.name, self.shouldAn, self.adjectives[0], self.adjectives[1], self.adjectives[2], self.gender, subPrint, self.race, self.background, self.charClass)

        #Attributes
        attributesString = "Str %i, Dex %i, Con %i, Int %i, Wis %i, Cha %i" %(self.attributes['Str'], self.attributes['Dex'], self.attributes['Con'], self.attributes['Int'], self.attributes['Wis'], self.attributes['Cha'])

        #Proficiencies
        proficienciesString = "Proficiencies: %s" %(", ".join(sorted(self.proficiencies)))

        return coreString + "\n" + attributesString + "\n" + proficienciesString + "\n"

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

"""
Robin = character()
#With this setup, we can create characters with certain parameters. But we should
#still be able to create characters with no attributes, too.
Robin.name = 'Robin'
Robin.race = 'Halfling'
Robin.subrace = 'Lightfoot'
Robin.proficiencies = ['Stealth', 'Sleight of Hand', 'Arcana']
print Robin
Robin.Str = Robin.roll4d6()
print Robin.Str
print Robin.Dex
print ""
"""

"""
Alpha = character(race = 'Halfling', charClass = 'Barbarian')
BetaDic = {'race':'Human', 'background':'Charlatan', 'charClass':'Bard', 'gender':'female'}
Beta = character(**BetaDic)
Gamma = character()
Delta = character()
Epsilon = character()

print Alpha
print Beta
print Gamma
print Delta
print Epsilon
"""
print character(race = "Half-Elf", charClass = "Barbarian", background="Sailor")

print character(race = "Half-Elf", charClass = "Barbarian", background="Sailor")

print character(race = "Half-Elf", charClass = "Barbarian", background="Sailor")

print character(race = "Half-Elf", charClass = "Barbarian", background="Sailor")

print character(race = "Half-Elf", charClass = "Barbarian", background="Sailor")
