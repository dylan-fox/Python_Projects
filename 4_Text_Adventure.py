#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The Goal: Remember Adventure? Well, we’re going to build a more basic version of that.
A complete text game, the program will let users move through rooms based on user input
and get descriptions of each room. To create this, you’ll need to establish the directions
in which the user can move, a way to track how far the user has moved (and therefore which
room he/she is in), and to print out a description. You’ll also need to set limits for how
far the user can move. In other words, create “walls” around the rooms that tell the user,
“You can’t move further in this direction.”
Concepts to keep in mind:
* Strings
* Variables
* Input/Output
* If/Else Statements
* Print
* List
* Integers
The tricky parts here will involve setting up the directions and keeping track of
just how far the user has “walked” in the game. I suggest sticking to just a few
basic descriptions or rooms, perhaps 6 at most. This project also continues to build
on using userinputted data. It can be a relatively basic game, but if you want to build
this into a vast, complex word, the coding will get substantially harder, especially if
you want your user to start interacting with actual objects within the game. That complexity
could be great, if you’d like to make this into a longterm project. *Hint hint.
"""
#----------------------------------------------------------------------------------------------------------------------------
import random
#First, let's start with a one dimensional, 4 room dungeon.
dungeon = ["entrance", "trapped room", "boss room", "treasure room"]
#print dungeon
#----------------------------------------------------------------------------------------------------------------------------
#A function for observing the current room; prints out the description of the room given.
def observe(playerPosition, bossHP):
    #print "You look around. You are in the", dungeon[playerPosition] + "."
    if playerPosition == 0:
        print "You find yourself in the entrance of a grim dungeon, it's damp walls dripping with mildew and blood."
    elif playerPosition == 1:
        print "The floors and walls show evidence of booby traps. Walk carefully, lest ye be killed."
    elif playerPosition == 2 and bossHP > 0:
        print "The guardian of this dungeon faces you, a mighty red dragon! If you move any closer, it might attack."
    elif playerPosition == 2 and bossHP <= 0:
        print "The dragon lies defeated. Beyond him, you can see the glimmer of treasure..."
    elif playerPosition == 3:
        print "You are surrounded by piles of gold, silver, and gems of inestimable value! You will surely die a rich man."
    else:
        print "You are in a computer program! Oh god!"

#----------------------------------------------------------------------------------------------------------------------------
#A function for walking. It takes the user's room as its argument.
#It tests if the user can walk where they want to, and if so, adjusts their position.
def walk(playerPosition, bossHP):
    direction = raw_input("Forward or backward?\n>>")
    if direction == 'forward':
        if playerPosition == len(dungeon) - 1:
            print "You can't walk any further."
            return playerPosition
        elif playerPosition == 2 and bossHP > 0:
            print "You can't proceed while the boss lives!"
            return playerPosition
        else:
            print "You walk further into the dungeon."
            return playerPosition + 1

    elif direction == 'backward':
        if playerPosition == 0:
            print "You're at the start of the dungeon."
            return playerPosition
        else:
            print "You walk towards the entrance."
            return playerPosition - 1

    else:
        print "You can't walk that direction."
        return playerPosition
#----------------------------------------------------------------------------------------------------------------------------
#Here's a function to warp to a certain room.
def teleport(playerPosition):
    destination = raw_input("Which room would you like to go to? You may choose entrance, trapped room, boss room, or treasure room.\n>>")
    if destination == 'entrance':
        return 0
    elif destination == 'trapped room':
        return 1
    elif destination == 'boss room':
        return 2
    elif destination == 'treasure room':
        return 3
    else:
        print "You can't teleport there."
        return playerPosition
#----------------------------------------------------------------------------------------------------------------------------
#Fight a boss!
def fight(playerPosition, playerHP, bossHP):
    #First check that the player is in the boss room with a live boss.
    if playerPosition != 2:
        print "There's no one to fight here."
        return (playerHP, bossHP)
    elif bossHP <= 0:
        print "The boss is dead."
        return (playerHP, bossHP)

    #Let's set the player's battle stats.
    playerAttack = 2
    playerHeal = 10

    #Next, enter a loop for as long as both the player and boss are alive.
    while playerHP > 0 and bossHP > 0:
        print "\nYou're fighting the boss! You have %i HP and it has %i HP." %(playerHP, bossHP)

        #Here's the user's action.
        action = raw_input("What do you do? You can attack, heal, or flee.\n>>")
        if action == 'attack':
            print "You strike a mighty blow, dealing %i damage." %playerAttack
            bossHP -= playerAttack
        elif action == 'heal':
            print "You call upon mighty healing magics, healing you %i HP." %playerHeal
            playerHP += playerHeal
        elif action == 'flee':
            print "You flee the fight."
            return (playerHP, bossHP)
        else:
            print "You stand there like an idiot."

        #And here's the boss's attack. If you're unlucky you get flamebreathed.
        bossAttackType = random.randint(1, 6)
        #1-3: claw
        if bossAttackType < 4:
            bossAttack = 2
            print "The boss reaches out with its terrible claws and hits you for %i damage!" %bossAttack
        #4-5: bite
        elif bossAttackType < 6:
            bossAttack = 4
            print "The boss bites you with its awful teeth, inflicting %i damage!" %bossAttack
        #6: fire breath
        elif bossAttackType == 6:
            bossAttack = 7
            print "The boss incinerates you with its fiery breath, dealing a whopping %i damage!" %bossAttack
        else:
            bossAttack = 0
            print "The boss glitches out, dealing no damage."
        playerHP -= bossAttack

    #Once either you or the boss have dropped to 0 hp, we end the battle and return the results.
    print "\nThe battle is over. "
    if playerHP <= 0:
        print "You have died. The boss had %i HP left." %bossHP
        return (playerHP, bossHP)
    elif bossHP <= 0:
        print "You killed the boss! You have %i HP left." %playerHP
        return (playerHP, bossHP)
    else:
        print "Something weird has happened. You have %i HP and the boss has %i HP left." %(playerHP, bossHP)
        return (playerHP, bossHP)
#----------------------------------------------------------------------------------------------------------------------------
#A function for quitting the dungeon. Unfortunately, you can't break the loop in the function definition.
def quit():
    print "You have escaped the dungeon... for now.\n"


#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

#Let's dungeon!

#The player starts at room 0, with 10 hp.
playerPosition = 0
playerHP = 10
bossHP = 20

print "Welcome to the dungeon."

#Take user action, as long as they have HP left.
while playerHP > 0:
    print "\nYou are in the", dungeon[playerPosition] + "."
    userAction = raw_input("What will you do next? You may observe, walk, fight, or quit.\n>>")

    if userAction == 'observe':
        observe(playerPosition, bossHP)

        #The player's position is updated by the walk function.
    elif userAction == 'walk':
        playerPosition = walk(playerPosition, bossHP)

    elif userAction == 'teleport':
        playerPosition = teleport(playerPosition)

    elif userAction == 'fight':
        playerHP, bossHP = fight(playerPosition, playerHP, bossHP)

    elif userAction == 'quit':
        quit()
        break

    else:
        print "That's not an option. Try again."

#Death message.
if playerHP <= 0:
    print "\nNo more adventuring for dead guys! You will be remembered fondly, like all those other jerks that died. Better luck next time."
