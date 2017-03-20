#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:04:16 2017

@author: mac
"""

'''
for
'''
l=[1,3,5,7,9,11,13]
for element in l[2:5]:
    print element**2
'''
range
'''
r=range(0,8,1)
r
type(r)
'''
for_range
'''
for i in range(2,5):
    print l[i]**2
'''
if_elif_else
'''
for i in range(1,10):
    if i%2==0:
        print '%d is even'%i
    elif i%3==0:
        print '%d is multiple of 3'%i
    else:
        print '%d is odd'%i
'''
while
'''
total =0
while total<100:
    total+=1
print total
'''
more over----------------list comprehension
'''
m=[i**2 for i in range(5)]
m
