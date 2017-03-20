#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:09:38 2017

@author: mac
"""

'''
review, type and guess
'''
a=10
type(a)
a.bit_lenghth()
'''
--------------
'''
1+4
1/4
type(1/4)
'''
--------------
'''
1./4
type(1./4)
c=0.2
c+0.2
b=0.35
b+0.1
'''
---------------
'''
import decimal
from decimal import Decimal
decimal.getcontext()
d=Decimal(1)/Decimal(11)
decimal.getcontext().prec=4
d=Decimal(1)/Decimal(11)
'''
----------------------------
'''
t='this is a sentence'
t.capitalize()
t.split()
t.find("sentence")
t.find('fuc')
t.replace(' ','|')
web='http://baidu.com'
web.strip('http://')
'''
more over------------------
'''
v=[0.5,0.75,1.0,1.5,2.0]
m=[v,v,v]
m
m[0][1]
v[0]='py'

from copy import deepcopy
v=[0.5,0.75,1.0,1.5,2.0]
m=3*[deepcopy(v),]
m
v[0]='py'

 '''
 -------------------------
 '''
import re
series='''
'01/18/2014 13:00:00',100,'1st';
'01/18/2014 13:30:00',110,'2nd';
'01/18/2014 14:00:00',120,'3rd'
'''
dt=re.compile("'[0-9/:\s]+'")
result=dt.findall(series)
'''
------------------------
'''
from datetime import datetime
pydt=datetime.strptime(result[0].replace("'",""),'%m/%d/%Y %H:%M:%S')
print pydt
type(pydt)
'''
--------------------------
'''
tu=1,2.5,'data'
tu.index(1)
