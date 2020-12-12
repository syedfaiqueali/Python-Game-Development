# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:06:59 2020

@author: Faique
"""

from random import *
from turtle import *

from base import vector

def value():
    # This will generate value from [-5,-3] to [3,5]
    
    # choice() either -1 or 1
    return (3+random()*2)*choice([-1,1])

# Setup the turtle console
ball = vector (0,0)
aim = vector(value(), value())

# Projection or movement from 'aim'

def draw():
    # Move the ball from aim and draw it on the screen
    ball.move(aim)

    x = ball.x
    y = ball.y
    
    # To check if ball hit the boundary
    if x < -200 or x > 200:
        aim.x = -aim.x  # Rotate the aim
        
    if y < -200 or y > 200:
        aim.y = -aim.y
    clear()
    goto(x,y)
    dot(10, 'Teal')
    ontimer(draw,50)
    


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
    
    
    