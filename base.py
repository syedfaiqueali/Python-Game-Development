# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:23:49 2020

@author: Faique
"""

import collections
import math
import os


def path(filename):
    # Return full path to 'filename'
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname((filepath))
    fullpath = os.path.join(dirpath, filename)
    return fullpath

def line(a,b,x,y):
    # Draw line from (a,b) to (x,y)
    import turtle 
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)
    

class Vector(collections.Sequence):
    # Seq in form of tuple (1,2)
    
    '''
    Two Dimentional Vector 
    Vectors can be modified in-place.
    
    v = vector(0,1)
    v.move(1)
    v
    vector(1,2)
    v.rotate(90)
    v
    vector(-2.0, 1.0)
    '''
    
    PRECESION = 6
    
    __slots__ = ('_x', '_y', '_hash') # Pass vector in it
    
    def __init__(self,x,y):
        # Initialize vector with coordinates: x, y
        '''
        v = vector(1,2)
        v.x => 1
        v.y => 2
        '''
        self._hash = None
        self._x = round(x, self.PRECESION)
        self._y = round(y, self.PRECESION)
        
        # Getter
        @property 
        def x(self):
            # X-axis component of vector
            return self._x
        
        # Setter
        def x(self, value):
            # To check if the hash is full or not
            if self._hash is not None:
                raise ValueError('cannot set x after hashing')
            self._x = round(value, self.PRECESION)
            
        @property
        def y(self):
            # Y-axis component of vector
            return self._y
        
        @y.setter
        def y(self, value):
            # To check if the hash is full or not
            if self._hash is not None:
                raise ValueError('cannot set y after hashing')
            self._y = round(value, self.PRECESION)
            
        def __hash__(self):
            '''
            v.__hash__() -> hash(v)
            
            v = vector(1,2)
            h = hash(v)
            v.x => 2
            
            Traceback(most recent call last):
                ...
            ValueError: cannot set x after hashing
            '''
            
            if self._hash is None:
                pair = (self.x, self.y)
                self._hash = hash(pair)
            return self._hash
        
        def __len__(self):
            '''
            v.__len__() -> len(v)
            
            v = vector(1,2)
            len(v) => 2
            '''
            return 2
        
        def __getitem__(self, index):
            '''
            v.__getitem__(v,i) -> v[i]
            
            v = vector(3,4)
            v[0] => 3
            v[1] => 4
            v[2] = Tracebacl(most recent call last):
                    ...
                   Index Error
            '''
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError
                
        def copy(self):
            '''
            Return copy of vector
            v = Vector(1,2)
            w = v.copy()
            v is w => False
            '''
            type_self = type(self)
            return type_self(self.x, self.y)
        
        # Equal to func
        def __eq__(self, other):
            '''
            v.__eq__(w) -> v == w
            v = vector(1,2)
            w = vector(1,2)
            v == w => True
            '''
            if isinstance(other,vector):
                return self.x == other.x and self.y == other.y # Bool type
            return NotImplemented
        
        # Not equal to func
        def __ne__(self, other):
            '''
            v.__ne__(w) -> v != w
            v = vector(1,2)
            w = vector(1,2)
            v != w => True
            '''
            if isinstance(other, vector):
                return self.x != other.x or self.y != other.y
            return NotImplemented
        
        def __iadd__(self, other):
            '''
            v.__iadd__(w) -> v += w
            v = vector(1,2)
            w = vector(3,4)
            v += w
            v  => vector(4,6)
            v += 1
            v => vector(5,7)
            
            '''
            if self._hash is not None:
                raise ValueError('cannot add vector after hashing')
            elif isinstance(other, vector):
                self.x += other.x
                self.y += other.y
            else:
                self.x += other
                self.y += other
            return self
        
        def __add__(self, other):
            '''
            v.__add__(w) -> v + w
             
            v = vector(1,2)
            w = vector(3,4)
            v + w
            vector(4,6)
            2.0 + v
            vector(3.0, 4.0)
            '''
            copy = self.copy()
            return copy.__iadd__(other)
        
        __radd__ = __add__
        
        def move(self, other):
            '''
            Move vector by other (in-place)
            
            v = vector(1,2)
            w = vector(3,4)
            v.move()
            v
            vector(4,6)
            v.move(3)
            v
            vector(7,9)
            '''
            self.__iadd__(other)
            
        def __isub__(self, other):
            '''
            v.__isub__(w) -> v -= w
            
            v = vector(1,2)
            w = vector(3,4)
            v -= w
            v
            vector(-2, -2)
            v -= 1
            v
            vector(-3,-3)
            '''
            
            if self._hash is not None:
                raise ValueError('cannot subtract vector after hashing')
            elif isinstance(other, vector):
                self.x -= other.x
                self.y -= other.y
            else:
                self.x -= other
                self.y -= other
            return self
                
        def __sub__(self, other):
            '''
            v.__sub__(w) -> v - w
            v = vector(1,2)
            w = vector(3.4)
            v - w
            vector(-2,-2)
            v - 1
            vector(0,1)
            '''
            copy = self.copy()
            return copy.__isub__(other)
            
        
    
