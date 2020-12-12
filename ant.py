# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:13:11 2020

@author: Faique
"""

from random import *
from turtle import *

from base import vector

# Instantiating a vector class object
ant = vector(0,0)

# Direction to move for the ant
aim  = vector(2,0)

# It would wrap and return us the value
def wrap(value):
    return value

# Draw function
def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(random() - 0.5) 
    
    aim.rotate(random()*10 - 5)
    clear() # TO clear turle console
    
    goto(ant.x, ant.y)
    dot(4)
    if running:
        ontimer(draw,100) # call draw() in every 100 mili sec
    

# Setup the turtle console
setup(420,420,370,0) # (width, height, startX, startY)
hideturtle()

# Turn turle animation on/off & set delay for update drawings
tracer(False) # False - no delay

up()

running = True
draw()
done()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

