# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 01:08:54 2018

@author: admin
"""

def rsum(n):
    if n <= 1:
        return n
    else:
        return n + rsum(n-1)

num = int(input("Enter a number: "))
ttl=rsum(num)
print("The sum is",ttl)