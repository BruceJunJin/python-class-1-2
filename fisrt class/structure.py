#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:22:58 2017

@author: mac
"""
'''
character string creating and print
''' 
str0='this is a sentence'
str1="this is a sentence too"
str2='''this is a sentence as well'''

print str0
print str1
print str2

'''
boolean type
'''
bool0=0>1;
bool1=1>0;
bool2=False
bool3=True;

print bool0
print bool1

'''
Numerical type
'''
a =20
b=float(a)
c=-2.3
print a,c,b
abs(c)
max(a,b,c)

'''
List
'''
list0=['physics', 'chemistry', 1997, 2000]
nums=[1, 3, 5, 7, 8, 13, 20]
#request
print nums[0]
print nums[0:4] #not include index 4
print nums[1:]
print nums[:-3]
#change
nums[0]='roger' 
print nums
#delete
del nums[0]
print nums
#inter lists operation
print [1,2,3]+[4,5,6] #cannot output [5,7,9] directly
print [1,2,3]*4
print 3 in [1, 2, 3]
for x in [1, 2, 3]: 
    print x
#inner list operation
#1.extend
nums.append(1)
print nums
nums.extend((2,3,5))
print nums
nums.insert(0,1)
print nums
#2.delete
nums.remove(1)
print nums
nums.pop()
print nums
nums.pop(4)
print nums
#3.others
nums.reverse()
nums.count(3)
nums.sort()#default is increasing 
max(nums)
min(nums)
len(nums)
cmp(nums,list0) #difference---  -1  same------- 0
cmp(nums,nums)
         
'''
Tuple
'''
tup1 = ('physics', 'chemistry', 1997, 2000) #try tup1[0]=1
#visit and operations are same with list, but tuple cannot change anyway
tup2 = (1, 2, 3, 4, 5 )
tup3=tup1+tup2
del tup2

'''
Dictionary
'''
info0= {'name': 'Bruce', 'age': 19, 'class': 'First'}
#request and the clear are same with list, but index is selfmade.
#operations
len(info0)
str(info0)
info0.clear()
info0= {'name': 'Bruce', 'age': 19, 'class': 'First'}
info0.copy()
info0.get('age') 
info0.get('First') 
info0.has_key('age')
info0.keys()
info0.values() 

'''
Date
'''
import time, datetime
time.localtime()
#transform
#time----str
print time.strftime('%Y-%m-%d %H:%M:%S')
print str(datetime.datetime.now())[:19]
#str-----time
expire_time = "2017-03-11 20:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
print d; #watch for the format of d;
