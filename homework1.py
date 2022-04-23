# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:46:58 2022

@author: Jonathan
"""

import matplotlib.pyplot as p
import numpy as np
import logistic_map_functions as lm


fig, axs = p.subplots(3,1)

map1a = lm.iterate_lm(2, 0.2, 500)
map2a = lm.iterate_lm(2, 0.200001, 500)

diffa = np.abs(map1a - map2a)

print(500, 2, diffa[-1])

axs[0].set_title('r=2')
axs[0].plot(diffa, 'o')

map1b = lm.iterate_lm(3.4, 0.2, 500)
map2b = lm.iterate_lm(3.4, 0.200001, 500)

diffb = np.abs(map1b - map2b)

print(500, 3.4, diffb[-1])

axs[1].set_title('r=3.4')
axs[1].plot(diffb, 'o')

map1c = lm.iterate_lm(3.72, 0.2, 500)
map2c = lm.iterate_lm(3.72, 0.200001, 500)

diffc = np.abs(map1c - map2c)

print (500, 3.72, diffc[-1])

axs[2].set_title('r=3.72')
axs[2].plot(diffc, 'o')


map1d = lm.iterate_lm(3.72, 0.2, 5000)
map2d = lm.iterate_lm(3.72, 0.200001, 5000)

diffd = np.abs(map1d - map2d)
aved = np.sum(diffd)/5000

print(5000, aved)

map1e = lm.iterate_lm(3.72, 0.2, 500000)
map2e = lm.iterate_lm(3.72, 0.200001, 500000)

diffe = np.abs(map1e - map2e)
avee = np.sum(diffe)/500000

print(500000, avee)