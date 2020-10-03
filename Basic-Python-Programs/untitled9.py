# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:52:41 2018

@author: admin
"""

def fib(n):
    a = 0
    b = 1
    c = a+b
    print(a,"\t",end = " ")
    for i in range(1,n+1):
        print(c,"\t",end = " ")
        c = a.a  +b
        a = b
        b = c
n = int(input())
print(fib(n))
