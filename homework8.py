# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:05:12 2022

@author: Jonathan
"""

import matplotlib.pyplot as p
import numpy as np

x = []

with open('amplitude.dat') as f:
    for line in f:
       x.append(float(line)) 

def embed(xs, tau, m, deltat=1):
    em = np.array(xs[:-tau*(m-1)])
    for q in range(1,m):
        app = xs[(tau*q)//deltat:-(m-q-1)*tau or None]
        em = np.column_stack((em,app))
    return em
            
m = embed(x, tau = 8, m = 7)


print(m.shape)
p.plot(m[:,0], m[:,2])             

            
ys = [1.2, 1.4, 1.1, 0.9, 0.5, 0.1, -0.2, 0.3, 0.4]

b = embed(ys, 2, 2)
m2 = embed(ys, 1, 3)
print(b)
print(m2)