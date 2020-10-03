# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:30:36 2018

@author: admin
"""

x = int(input("enter number"))
Range = int(input("enter range"))
sum = 1
for i in range(2,Range+1):
    sum = sum + x**i/i
print(sum)