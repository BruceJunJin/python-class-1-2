#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:02:19 2017

@author: mac
"""

'''
techique
'''

'''
Data in
'''
import numpy as np
import pandas as pd
import pandas_datareader.data as web 
import matplotlib.pyplot as plt

sp500=web.DataReader('^GSPC',data_source='yahoo',start='1/1/2010')
#,end='4/14/2014'
#sp500.info()
#sp500.tail()

'''
ezplot
'''
sp500['Close'].plot(grid=True,figsize=(8,5))

'''
trend analysis
'''
sp500['42d']=np.round(pd.rolling_mean(sp500['Close'],window=42),2)
sp500['252d']=np.round(pd.rolling_mean(sp500['Close'],window=252),2)
#sp500.head()

'''
trend ezplot
'''
sp500[['Close','42d','252d']].plot(grid=True,figsize=(8,5))

'''
Strategy forming (Signal Determination strategy)
'''
sp500['42-252']=sp500['42d']-sp500['252d']
#sp500['42-252']
#Regime basic look
SD=50
sp500['Regime']=np.where(sp500['42-252']>SD,1,0)
sp500['Regime']=np.where(sp500['42-252']<-SD,-1,sp500['Regime'])
sp500['Regime'].value_counts()

'''
Cross Signal
'''
sp500['Regime'].plot(lw=1.5)
plt.ylim([-1.1,1.1])
plt.grid(True)
plt.show()

'''
Test (hypothesis)
'''
#market log-return 
sp500['Market']=np.log(sp500['Close']/sp500['Close'].shift(1))
#mockery
sp500['Strategy']=sp500['Regime'].shift(1)*sp500['Market']
#compare
sp500[['Market','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
plt.show()