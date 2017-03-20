#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:00:58 2017

@author: mac
"""

import numpy as np
dt=np.dtype([
        ('name','S10'),
        ('age','i4'),
        ('height','f8'),
        ('children/pets','i4',2)])
s=np.array([('smith',45,1.83,(0,1)),
           ('jones',53,1.76,(2,2))],
           dtype=dt)
#visit
s['name']
s['height'].mean()