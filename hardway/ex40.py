"""
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy brithday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
"""

class character:
    name = ''
    race = ''
    subrace = ''
    skills = []
    Str = 0
    Dex = 0
    Con = 0
    Int = 0
    Wis = 0
    Cha = 0
    level = 1
    profiency = 2

    def description(self):
        charDescription = "%s is a level %d %s %s. \nSkills: %s" %(self.name, self.level, self.subrace, self.race, ", ".join(sorted(self.skills)))
        return charDescription

Robin = character()
Robin.name = 'Robin'
Robin.race = 'Halfling'
Robin.subrace = 'Lightfoot'
Robin.skills = ['Stealth', 'Sleight of Hand', 'Arcana']
print Robin.description()
