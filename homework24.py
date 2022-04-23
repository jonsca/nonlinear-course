# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 06:01:15 2022

@author: Jonathan
"""

import logistic_map_functions as lm

xb1, yb1 = lm.bifurcation_values(0.2, 2.990, 3.001, 0.01, 1000,500)
xb2, yb2 = lm.bifurcation_values(0.2, 3.425, 3.475, 0.005, 1000, 800)
xb3, yb3 = lm.bifurcation_values(0.2, 3.53, 3.56, 0.005, 1000, 800)

b1 = 3
b2 = 3.4494
b3 = 3.5444

feig = (b2 - b1)/(b3-b2)

print(f'Feigenbaum is approximately {feig}')