# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex5.html

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
unit_height = ["cm", "inches"]
unit_weight = ["kg", "pounds"]

unit = 1

if (unit == 0):
	height = height * 2.54 # cm
	weight = weight * 0.45359237 # kg
	

print "Let's talk about %s." % name
print "He's %d %s tall." % (height, unit_height[unit]) # inches or cm
print "He's %d %s heavy." % (weight, unit_weight[unit]) # pounds or kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)