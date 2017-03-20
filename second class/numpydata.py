#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:52:52 2017

@author: mac
"""
import numpy as np
a=np.array([0,0.5,1.0,1.5,2.0])
type(a)
a[:2]
#inner
a.sum()
a.std()
a.cumsum()
#vectorize
a*2
a**2
np.sqrt(a)
#continu
b=np.array([a,a**2])
b[0]
b[0,2]
b.sum()
b.sum(axis=0)
b.sum(axis=1)
#initalize
c=np.zeros((2,3,4),dtype='i',order='C')
c=np.zeros((2,3,4),dtype='f',order='C') #np.ones()

#speed
import random as rd
I=5000
mat=[[rd.gauss(0,1) for j in range(I)] for i in range(I)]
reduce(lambda x,y :x+y, [reduce(lambda x,y :x+y,row) for row in mat])

#versus
import numpy as np
mat=np.random.standard_normal((I,I))
mat.sum()
