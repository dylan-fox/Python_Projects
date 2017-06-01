name = 'Dylan Fox'
age = 25.0 #truth
height = 72.0 #inches
weight = 230.0 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Dark Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)

#calculate metric measures
metricHeight = round(2.54*height, 2)
metricWeight = round(0.453592*weight, 2)
print metricHeight
print metricWeight
print "Those units used the imperial system. If you want metric, he's %s cm tall and %s kilograms." % (metricHeight, metricWeight)
