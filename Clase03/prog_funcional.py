'''
Created on 3 sep. 2016

@author: python
'''
from functools import *
def por2(num):
    return num*2

a=list(map(lambda x: x**2,[2,3,4]))

b=reduce((lambda x,y:x+y),[1,2,3,4,5])
#for x in a:
 #   print((x))
    
print(b)
    
