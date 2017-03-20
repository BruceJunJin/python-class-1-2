#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:02:50 2017

@author: mac
"""
'''
Monte Carlo valuation of European call with pure python
'''
from time import time
from math import exp, sqrt, log
from random import seed, gauss
seed(20000)
t0=time()

#parametres
s0=100 #initial value
K=105 #knocking price
T=1.0 #maturity
r=0.05 #rf
sigma=0.2 #volatility
M=50 #50times simulate
dt=T/M
I=250000 #number of paths

#simulate
s=[]
for i in range(I):
    path=[]
    for t in range(M+1):
        if t==0 :
            path.append(s0)
        else :
            z= gauss(0.0,1.0)
            St= path[t-1]*exp((r-0.5*sigma**2)*dt+sigma*sqrt(dt)*z)
            path.append(St)
    s.append(path)
#calculating
C0=exp(-r*T)*sum([max(path[-1]-K,0) for path in s])/I
#result output
tpy=time()-t0
print "Option Value is %7.3f" % C0
print "Finished in %7.3f seconds" % tpy

'''
Possibility of ameliorating
---------------------------
#calculating part
sum_val=0.0
for path in S:
    sum_val+=max(path[-1]-K,0)
    C0=exp(-r*T)*sum_vsl/I
    round(C0,3)
'''