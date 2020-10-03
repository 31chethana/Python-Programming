# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 00:50:19 2018

@author: admin
"""


def mUl(x):
   if x<=1:
       return x
   else:      
       return int(x) + mUl(x-1)
x = int(input("enter number"))
print(mUl(x))