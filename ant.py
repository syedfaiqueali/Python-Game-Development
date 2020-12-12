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
    aim.move(random() - 0.5) # 0.5 speed
    aim.rotate(random()*10 - 5)
    clear() # TO clear turle console
    goto(ant.x, ant.y)
    
    # (radius, color)
    dot(5, 'black') 
    if running:
        ontimer(draw,100) # call draw() in every 100 mili sec
    

# Setup the turtle console
# (width, height, startX, startY)
setup(420,420,370,0) 
hideturtle()

# Turn turle animation on/off & set delay for update drawings
tracer(False) # False - no delay

# Don't draw while up
up()

running = True

# Calling our draw function
draw()
# We have exited out our turtle module
done()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

