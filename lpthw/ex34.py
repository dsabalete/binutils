# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex34.html

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
ordinal = ['first', 'second', 'third', 'fourth', 'fiveth', 'sixth']

def printAnimal(n):
    print "The %s animal is at %d and is a %s." % (ordinal[n], n, animals[n]),
    print "The animal at %d is the %s animal and is a %s." % (n, ordinal[n], animals[n])
    
printAnimal(1)
printAnimal(2)
printAnimal(0)
printAnimal(3)
printAnimal(4)
printAnimal(2)
printAnimal(5)
printAnimal(4)