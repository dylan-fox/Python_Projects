tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

"""
#Trying out some escape sequences.
experiment = '''
\\ backslash
\' single quote
\" double quote
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\r carriage return
\t Horizontal tab (TAB)
u'\U0001F47E' 16 bit hex value
\v ASCII vertical tab
\ooo character with octal value ooo
\x22 character with hex value hh
'''
#\N{} Unicode database
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#print experiment
print tabby_cat + "\r" + persian_cat
print "123456\r789"
print "1234\b567"
