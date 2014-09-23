# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex6.html

# Variable setting
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # string inside string

# Printing vars x and y
print x
print y # string inside string

# Printing var x and y inside a string
print "I said: %r." % x 		# string inside string
print "I also said: '%s'." % y 		# string inside string

# more variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# evaluate boolean value inside a string var
print joke_evaluation % hilarious

# and more string vars
w = "This is the left side of..."
e = "a string with a right side."

# printing them easely by concatenating them
print w + e
