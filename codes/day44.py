"""
list=[1,2,3,4,5,5,5,5]
x= set(list)
print(x)
x.add()
x.remove()
x.pop() #### without index (set is unordered)
########################

def test(**x):
    print(x) ##### print it as dic
    print(x["name"])
    print(*x) ###### print keys

test(name="omar",age="30")

def display(*args,**kword):
    print("posisional: ",args)
    print("keyword argument: ",kword)
    
display(1,2,3,name="alice",age="30")
display(1,2,3,name=[1,2,3,4],age="30")"

l=[x**2 for x in range(10) if x %2 == 0]
print(l)"

fruits=["apple","banana","cherry"]
for index , fruit in enumerate(fruits):
    print(index,fruit)"

from modulesss.helper import pi
import re 
import math 
........................................................................

import pandas as pd
data=[{},{}]
df=pd.dataframe(data)
print(df)
..........................................................................."

try:
    print(1/0)
except: 
    print("error")
print("end")

raise("error") ####### if i need ro close the system (return- break) and return error
"""

