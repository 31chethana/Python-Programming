# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:25:23 2018

@author: admin
"""

class Rectangle:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def Area(self):
        a = self.length*self.breath
        print("area is",a)
f1 = Rectangle(2,3)
f2 = Rectangle(2,3)
f1.Area()
f2.Area()