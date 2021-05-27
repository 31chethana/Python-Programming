# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:29:57 2018

@author: admin
"""
a = input("enter letter" )
count = 0
c = len(a)-1
for i in range(0,len(a)):
    if a[i] == a[c]:
        count+= 1
        c-= 1
if count == len(a):
    print("palidrome")
else:
    print("not")