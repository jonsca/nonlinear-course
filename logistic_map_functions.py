# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:25:07 2022

@author: Jonathan
"""

import numpy as np

def logistic_map(r, x_n):
    return r*x_n*(1 - x_n)

def iterate_lm (r, x_0, n):
    x_last = x_0
    result = np.zeros(n)
    for i in range(0,n):
        x_n = logistic_map(r, x_last)
        result[i] = x_n
        x_last = x_n

    return result

def bifurcation_values(x_0, r_min, r_max, r_step, n, k):
    x = []
    y = []
    for r in np.arange(r_min, r_max, r_step):
        y_vals = iterate_lm(r, x_0, n)[k:]
        for val in y_vals:
            x.append(r)
            y.append(val)
           
    return np.array(x),np.array(y)