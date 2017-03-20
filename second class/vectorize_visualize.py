# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
from time import time
np.random.seed(20000)
t0=time()

#parametres
s0=100
K=105
T=1.0
r=0.05
sigma=0.2
M=50
dt=T/M
I=250000

#simulate
s=s0*np.exp(np.cumsum((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*np.random.standard_normal((M+1,I)),axis=0))
s[0]=s0
c0=np.exp(-r*T)*sum(np.maximum(s[-1]-K,0))/I
typ2=time()-t0

print "Option value is %7.3f " % c0
print "Finished in %7.3f second" % typ2

'''
visualize
'''

'''
path
'''
import matplotlib.pyplot as plt
plt.plot(s[:,:10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')
plt.show()
'''
tail state
'''
plt.hist(s[-1],bins=50)
plt.grid(True)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.ylim(0,30000)
plt.show()
'''
inner value
'''
plt.hist(np.maximum(s[-1]-K,0),bins=50)
plt.grid(True)
plt.xlabel('inner value')
plt.ylabel('frequency')
plt.ylim(0,50000)
plt.show()