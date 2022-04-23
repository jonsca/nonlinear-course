# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:26:45 2022

@author: Jonathan
"""


import matplotlib.pyplot as p
import logistic_map_functions as lm

x,y = lm.bifurcation_values(0.2, 3.50, 3.6, 0.01, 1000, 500)

p.scatter(x, y, s=2)








