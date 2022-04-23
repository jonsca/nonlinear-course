# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 01:52:12 2022

@author: Jonathan
"""

import numpy as np
import matplotlib.pyplot as p

vars = np.loadtxt('CapDimData.dat', delimiter=',')

eps = 0.05

x = vars[:,0]
z = vars[:,2]
length = x.shape[0]
minx = x.min()
minz = z.min()
maxx = x.max()
maxz = z.max()

xcount = int(np.ceil((maxx - minx)/eps)) + 1
zcount = int(np.ceil((maxz - minz)/eps)) + 1

print(xcount)
print(zcount)

matrix = np.zeros(shape=(xcount, zcount))

for i in range(length):
    xcor = int(np.ceil((x[i] - minx)/eps))
    zcor = int(np.ceil((z[i] - minz)/eps))
    matrix[xcor, zcor] = 1
   
matnorm = sum(sum(matrix))
print(matnorm)




