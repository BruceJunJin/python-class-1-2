#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:17:26 2017

@author: mac
"""
'''
basic
'''
def f(x):
    return x**2
'''
progress
'''
def even(x):
    return x%2==0
'''
lambda
'''
lambda x: x**2
'''
map
'''
map(even,range(10))
map(lambda x: x**2,range(10))
'''
filter
'''
filter(even,range(15))
'''
reduce
'''
reduce(lambda x,y: x+y, range(10))

