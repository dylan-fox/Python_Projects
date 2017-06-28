#!/usr/bin/env python
# -*- coding: utf-8 -*-
#A program to generate random 5th edition NPCs.
import random

"""
Let's start by generating 10 random characters.
We need to give their:
* Race
* Background
* Class
* Ability Scores
* Skills
* Appearance
* Backstory

We can determine race, background, and class at random.
Ability scores and skills should be based on that.
Appearance and backstory can be essentially random for now.
"""

def randomChar():
    """Generates a random character's race, subrace, background, and class."""
    #Generate a random number between 1 and 9, then reassign race based on that number.
    race = random.randint(1, 9)
    if race == 1:
        race = "Dragonborn"
        subrace = random.randint(1,10)
        if subrace == 1:
            subrace ="Black"
        elif subrace == 2:
            subrace ="Blue"
        elif subrace ==3:
            subrace ="Brass"
        elif subrace ==4:
            subrace = "Bronze"
        elif subrace ==5:
            subrace = "Copper"
        elif subrace ==6:
            subrace = "Gold"
        elif subrace == 7:
            subrace = "Green"
        elif subrace == 8:
            subrace = "Red"
        elif subrace == 9:
            subrace = "Silver"
        elif subrace == 10:
            subrace = "White"

    elif race == 2:
        race = "Dwarf"
        subrace = random.randint(1,2)
        if subrace == 1:
            subrace = "Hill"
        else:
            subrace = "Mountain"

    elif race == 3:
        race = "Elf"
        subrace = random.randint(1,5)
        if subrace == 1 or subrace == 2:
            subrace = "High"
        elif subrace == 3 or subrace == 4:
            subrace = "Wood"
        elif subrace == 5:
            subrace = "Drow"

    elif race == 4:
        race = "Gnome"
        subrace = random.randint(1,2)
        if subrace == 1:
            subrace = "Forest"
        elif subrace == 2:
            subrace = "Rock"

    elif race == 5:
        race = "Half-Elf"
        subrace = ""

    elif race == 6:
        race = "Half-Orc"
        subrace = ""

    elif race == 7:
        race = "Halfling"
        subrace = random.randint(1,2)
        if subrace == 1:
            subrace = "Lightfoot"
        elif subrace == 2:
            subrace = "Stout"

    elif race == 8:
        race = "Human"
        subrace = ""

    elif race == 9:
        race = "Tiefling"
        subrace = ""

    background = random.randint(1, 13)
    if background == 1:
        background = "Acolyte"
    elif background == 2:
        background = "Charlatan"
    elif background == 3:
        background = "Criminal"
    elif background == 4:
        background = "Entertainer"
    elif background == 5:
        background = "Folk Hero"
    elif background == 6:
        background = "Guild Artisan"
    elif background == 7:
        background = "Hermit"
    elif background == 8:
        background = "Noble"
    elif background == 9:
        background = "Outlander"
    elif background == 10:
        background = "Sage"
    elif background == 11:
        background = "Sailor"
    elif background == 12:
        background = "Soldier"
    elif background == 13:
        background = "Urchin"

    charClass = random.randint(1, 12)
    if charClass == 1:
        charClass = "Barbarian"
    elif charClass == 2:
        charClass = "Bard"
    elif charClass == 3:
        charClass = "Cleric"
    elif charClass == 4:
        charClass = "Druid"
    elif charClass == 5:
        charClass = "Fighter"
    elif charClass == 6:
        charClass = "Monk"
    elif charClass == 7:
        charClass = "Paladin"
    elif charClass == 8:
        charClass = "Ranger"
    elif charClass == 9:
        charClass = "Rogue"
    elif charClass == 10:
        charClass = "Sorcerer"
    elif charClass == 11:
        charClass = "Warlock"
    elif charClass == 12:
        charClass = "Wizard"

    return race, subrace, background, charClass

#-------------------------------------------------------------------------------

def roll4d6():
    """Generates an ability score by rolling 4d6 and dropping the lowest."""
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    sortedRolls = sorted([roll1, roll2, roll3, roll4])
    return sortedRolls[1] + sortedRolls[2] + sortedRolls[3]

#-------------------------------------------------------------------------------

def AbilityScores(race, subrace, charClass):
    """Generate ability scores based on race, subrace, and class."""
    #Let's roll 4d6 and drop the lowest for each score.
    #Then rank the scores from best to worst.
    #Then assign scores based on class.
    #Then modify scores based on race.
    sortedScores = sorted([roll4d6(), roll4d6(), roll4d6(), roll4d6(), roll4d6(), roll4d6()])
    score1 = sortedScores[0]
    score2 = sortedScores[1]
    score3 = sortedScores[2]
    score4 = sortedScores[3]
    score5 = sortedScores[4]
    score6 = sortedScores[5]

    otherScores = [sortedScores[0], sortedScores[1], sortedScores[2], sortedScores[3], sortedScores[4]]
    highScore = sortedScores[5]
    random.shuffle(otherScores)

    #Ideally each of these has 1 high attribute, and the rest are divvied up at random.
    #Strength classes
    if charClass == "Barbarian" or charClass == "Fighter" or charClass == "Paladin" or charClass == "Monk":
        Str = highScore
        Dex = otherScores[0]
        Con = otherScores[1]
        Int = otherScores[2]
        Wis = otherScores[3]
        Cha = otherScores[4]
    #Dex classes
    elif charClass == "Rogue" or charClass == "Ranger":
        Str = otherScores[0]
        Dex = highScore
        Con = otherScores[1]
        Int = otherScores[2]
        Wis = otherScores[3]
        Cha = otherScores[4]
    #Int classes
    elif charClass == "Wizard":
        Str = otherScores[0]
        Dex = otherScores[2]
        Con = otherScores[1]
        Int = highScore
        Wis = otherScores[3]
        Cha = otherScores[4]
    #Wis classes
    elif charClass == "Cleric" or charClass == "Druid":
        Str = otherScores[0]
        Dex = otherScores[2]
        Con = otherScores[1]
        Int = otherScores[3]
        Wis = highScore
        Cha = otherScores[4]
    #Cha classes
    elif charClass == "Bard" or charClass == "Warlock" or charClass == "Sorcerer":
        Str = otherScores[0]
        Dex = otherScores[2]
        Con = otherScores[1]
        Int = otherScores[3]
        Wis = otherScores[4]
        Cha = highScore

    #Adjust for race.
    if race == "Dragonborn":
        Str +=2
        Cha +=1
    elif race == "Dwarf":
        if subrace == "Hill":
            Wis +=1
        elif subrace == "Mountain":
            Str +=2
    elif race == "Elf":
        Dex +=2
        if subrace == "High":
            Int +=1
        elif subrace == "Wood":
            Wis +=1
        elif subrace == "Drow":
            Cha +=1
    elif race == "Gnome":
        Int +=2
        if subrace == "Forest":
            Dex +=1
        elif subrace == "Rock":
            Con +=1
    elif race == "Half-Elf":
        Cha +=2
        #print "Stats before boost: %i %i %i %i %i %i" %(Str, Dex, Con, Int, Wis, Cha)
        raceBoost = random.sample([1, 2, 3, 4, 5], 2)
        if raceBoost[0] == 1 or raceBoost[1] == 1:
            Str +=1
            #print "Boosted Str"
        if raceBoost[0] == 2 or raceBoost[1] == 2:
            Dex +=1
           #print "Boosted Dex"
        if raceBoost[0] == 3 or raceBoost[1] == 3:
            Con +=1
            #print "Boosted Con"
        if raceBoost[0] == 4 or raceBoost[1] == 4:
            Int +=1
            #print "Boosted Int"
        if raceBoost[0] == 5 or raceBoost[1] == 5:
            Wis +=1
            #print "Boosted Wis"
        #print "Stats after boost: %i %i %i %i %i %i" %(Str, Dex, Con, Int, Wis, Cha)

    elif race == "Half-Orc":
        Str +=2
        Con +=1

    elif race == "Halfling":
        Dex +=2
        if subrace == "Lightfoot":
            Cha +=1
        elif subrace == "Stout":
            Con +=1

    elif race == "Human":
        raceBoost = random.sample([1, 2, 3, 4, 5, 6], 2)
        if raceBoost[0] == 1 or raceBoost[1] == 1:
            Str +=1
            #print "Boosted Str"
        if raceBoost[0] == 2 or raceBoost[1] == 2:
            Dex +=1
            #print "Boosted Dex"
        if raceBoost[0] == 3 or raceBoost[1] == 3:
            Con +=1
            #print "Boosted Con"
        if raceBoost[0] == 4 or raceBoost[1] == 4:
            Int +=1
            #print "Boosted Int"
        if raceBoost[0] == 5 or raceBoost[1] == 5:
            Wis +=1
           #print "Boosted Wis"
        if raceBoost[0] == 6 or raceBoost[1] == 6:
            Cha +=1
            #print "Boosted Cha"

    elif race == "Tiefling":
        Int +=1
        Cha +=2

    return Str, Dex, Con, Int, Wis, Cha

#-------------------------------------------------------------------------------

def randomSkill(quantity):
    """Returns a given number of random skills."""
    skillRange = range(1,19)
    bonusSkills = random.sample(skillRange, quantity)
    skills = []
    if 1 in bonusSkills:
        skills += ["Athletics"]
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

#-------------------------------------------------------------------------------

def skills(race, subrace, background, charClass):
    """Assign skills based on race, background, and class."""

    skills = []

    #classes
    if race == "Dwarf":
        skills +=["Artisan's tools"]
    elif race == "Half-Orc":
        skills +=["Intimidate"]
    elif race == "Elf":
        skills += ["Perception"]
    elif race == "Gnome" and subrace == "Rock":
        skills += ["Tinker's tools"]
    elif race == "Half-Elf":
        skills += randomSkill(2)
    elif race == "Half-Orc":
        skills += ["Intimidate"]
    elif race == "Human":
        skills += randomSkill(1)

    #backgrounds
    if background == "Acolyte":
        skills +=["Insight", "Religion"]
    if background == "Charlatan":
        skills +=["Deception", "Sleight of Hand", "Disguise Kit", "Forgery Kit"]
    if background == "Criminal":
        skills +=["Deception", "Stealth", "Gaming Set", "Thieves' Tools"]
    if background == "Entertainer":
        skills +=["Acrobatics", "Performance", "Musical Instrument", "Disguise Kit"]
    if background == "Folk Hero":
        skills +=["Animal Handling", "Survival", "Artisan's Tools", "Land Vehicles"]
    if background == "Guild Artisan":
        skills +=["Insight", "Persuasion", "Artisan's Tools"]
    if background == "Hermit":
        skills +=["Medicine", "Religion", "Herbalism Kit"]
    if background == "Noble":
        skills +=["History", "Persuasion", "Gaming Set"]
    if background == "Outlander":
        skills +=["Athletics", "Survival", "Musical Instrument"]
    if background == "Sage":
        skills +=["Arcana", "History"]
    if background == "Sailor":
        skills +=["Athletics", "Perception", "Navigator's Tools", "Water Vehicles"]
    if background == "Soldier":
        skills +=["Athletics", "Intimidation", "Gaming Set", "Land Vehicles"]
    if background == "Urchin":
        skills +=["Sleight of Hand", "Stealth", "Disguise Kit", "Thieves' Tools"]

    #classes
    if charClass == "Barbarian":
        newSkills = random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Bard":
        skills += randomSkill(3)
    elif charClass == "Cleric":
        newSkills = random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Druid":
        newSkills = random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Fighter":
        newSkills = random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Monk":
        newSkills = random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Paladin":
        newSkills = random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Ranger":
        newSkills = random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3)
        skills +=[newSkills[0], newSkills[1], newSkills[2]]
    elif charClass == "Rogue":
        newSkills = random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4)
        skills +=[newSkills[0], newSkills[1], newSkills[2], newSkills[3]]
    elif charClass == "Sorcerer":
        newSkills = random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Warlock":
        newSkills = random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2)
        skills +=[newSkills[0], newSkills[1]]
    elif charClass == "Wizard":
        newSkills = random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2)
        skills +=[newSkills[0], newSkills[1]]

    #Replace duplicates with random skills

    #sort list
    sortedSkills = sorted(skills)
    return sortedSkills


#-------------------------------------------------------------------------------

for x in range(1, 11):
    char = randomChar()
    race = char[0]
    subrace = char[1]
    background = char[2]
    charClass = char[3]

    abilities = AbilityScores(race, subrace, charClass)
    charSkills = skills(race, subrace, background, charClass)
    print x, "%s %s %s %s" %(subrace, race, background, charClass)
    print "\tStr %i Dex %i Con %i Int %i Wis %i Cha %i" %abilities
    #print "\tSkills: %s" %(charSkills)
    print '\tSkills: %s' % ', '.join(map(str, charSkills))
    print "\n"
