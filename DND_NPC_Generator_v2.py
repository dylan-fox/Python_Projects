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
        self.randomName(self.race, self.gender)
        self.age = 0
        self.proficiencies = []
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
    def __str__(self):
        """Returns the description of the character."""
        if self.subrace == None:
            return "%s is a %s level %d %s %s %s. \nProficiencies: %s\n" %(self.name, self.gender, self.level, self.race, self.background, self.charClass, ", ".join(sorted(self.proficiencies)))
        else:
            return "%s is a %s level %d %s %s %s %s. \nProficiencies: %s\n" %(self.name, self.gender, self.level, self.subrace, self.race, self.background, self.charClass, ", ".join(sorted(self.proficiencies)))

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
#Robin.randomSubRace()
Robin.proficiencies = ['Stealth', 'Sleight of Hand', 'Arcana']
print Robin
Robin.Str = Robin.roll4d6()
print Robin.Str
print Robin.Dex
print ""
"""

Alpha = character(race = 'Halfling', charClass = 'Rogue')
Beta = {'race':'Human', 'background':'Charlatan', 'charClass':'Bard', 'gender':'female'}
Beta = character(**Beta)
Gamma = character()
Delta = character()
Epsilon = character()

print Alpha
print Beta
print Gamma
print Delta
print Epsilon
