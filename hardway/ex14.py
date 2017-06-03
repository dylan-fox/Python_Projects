#You really learn this one thing at a time, and when you look back, you've climbed a mountain.
from sys import argv

script, user_title, user_name = argv
prompt = 'Talk to me: '

print "Hi %s, I'm the %s script." %(user_name, script)
print "Oh, excuse me; I meant to use your official title, %s %s" %(user_title, user_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright %s %s, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" %(user_title, user_name, likes, lives, computer)
