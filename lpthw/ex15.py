# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex15.html

# import feature argv from package sys
from sys import argv

# extract values packed in argv
script, filename = argv

# open file which name is in filename var
txt = open(filename)

# Nice output
print "Here's your file %r:" % filename
# File content output
print txt.read()
txt.close()

# Nice output again
#print "Type the filename again:"

# Asking the name of the file to the user
#file_again = raw_input("> ")

# Open the file named by user
#txt_again = open(file_again)

# File content output
#print txt_again.read()
#txt_again.close()
