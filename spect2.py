# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:09:13 2017

@author: janmesh007
"""
import numpy as np
import matplotlib.pyplot as plt


with open("test.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

result = [float(x.strip("'")) for x in content]
    
initE = 2
nDots = 20
val = np.linspace(0, 0, nDots)
t = np.linspace(0, initE, nDots)

diffE = []
count = 0

while (count < len(result)):
	diffE.append(initE - result[count])
	count = count + 1
 
i = 0
j = 0 

while j < len(diffE):
    while i < (len(t)-1):
        if (t[i] <= diffE[j] < t[i+1]):
            val[i] += 1

        i += 1
    i = 0
    j += 1
 
#print(val, t)
 
plt.plot(t, val/max(val),'r')
plt.ylabel(" Relative Counts")
plt.xlabel("Energy") 


print(val[0]) 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
