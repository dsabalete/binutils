# -*- coding: UTF-8 -*-
# http://learnpythonthehardway.org/book/ex36.html

from sys import exit

def puertaA():
    print "puerta A"


def puertaB():
    print "puerta B"


def fin(msg):
    print msg, "Buen trabajo!"
    exit(0)


def start():
    print "Estas en una habitacion oscura"
    print "Hay dos puertas: A - blanca y B - negra"
    print "Que puerta escojeras?"
    
    choice = raw_input("> ")
    
    if choice == "A":
        puertaA()
    elif choice == "B":
        puertaB()
    else:
        fin("Te quedas dando vueltas en la habitacion hasta que mueres.")
    
    
start()