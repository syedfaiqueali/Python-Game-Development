# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:12:43 2020

@author: Faique
"""

from random import *
from turtle import *

from base import vector

ball = vector(-200,-200)

# Initially speed is zero depends on user when he taps
speed = vector(0,0)

targets = []

def inside(xy):
    # Return(Bool)
    # False - Strike with the boundary
    return -200 < xy.x < 200 and -200 < xy.y <200

def tap(x,y):
    # Respond to the screen, only 1 ball at a time
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25        

def draw():
    # Draw ball and targets
    clear() # If any obj in the console
    
    for target in targets:
        goto(target.x, target.y)
        dot(20,'blue')
        
    if inside(ball):
        ''' When we tap so it will go on to that position
            and show the dot '''
        goto(ball.x, ball.y)
        dot(6, 'red')
    
    update()
        
    

def move():
    # Movement of ball and target
    
    # 0-40 - define stop limit
    if randrange(40) == 0:
        # Y range between -150 -> 150
        y = randrange(-150,150)
        
        # X positon is constant because only y moving
        target = vector(200,y)
        
        # Append to the target array
        targets.append(target)
        
    for target in targets:
        target.x -= 0.5 
    
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    
    dupe = targets.copy()
    targets.clear()
    
    for target in dupe:
        if abs(target - ball) > 5:
            targets.append(target)
    
    draw()
        
    for target in targets:
        if not inside(target):
            return 
    
    ontimer(move, 50)
    


# Setup the turtle console
# (width, height, startX, startY)
setup(420,420,370,0) 

hideturtle()
up()

# Turn turle animation on/off & set delay for update drawings
tracer(False) # False - no delay

# WIll fire on screen click
onscreenclick(tap)

# Calling the move func
move()

done()

