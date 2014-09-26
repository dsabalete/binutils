# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex13.html

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third vairable is:", third

jander = raw_input("¿Y ahora qué? ")
print "Se acabó", third, jander
