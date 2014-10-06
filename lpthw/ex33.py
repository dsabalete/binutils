# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex33.html

def runNumbers(n, inc):
    i = 0
    numbers = []
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + inc
        print "Numbers now ", numbers
        print "At the bottom i is %d" % i
        
    print "The numbers: "
    
    for num in numbers:
        print num    


def runNumbersFor(n, inc):
    numbers = []
    for i in range(0, n, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now ", numbers
        print "At the bottom i is %d" % i
        
    print "The numbers: "
    
    for num in numbers:
        print num    
        
        
# runNumbers(10, 2)
runNumbersFor(10, 2)