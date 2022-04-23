# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 06:17:39 2022

@author: Jonathan
"""


def x_prime(v):
    return v

def v_prime(x, k=2, m=0.5, beta = 0, v=0): 
    return -x*(k/m) - beta*v

def forward_step(x_n, v_n, deltat):

    return x_n + deltat*x_prime(v_n), v_n + deltat*v_prime(x_n)

def backward_step(x_n, v_n, deltat):
    x_step, v_step = forward_step(x_n, v_n, deltat)
    
    return x_n + deltat*x_prime(v_step), v_n + deltat*v_prime(x_step)

def combined_step(x_n, v_n, deltat):
    x_original = x_prime(v_n)
    v_original = v_prime(x_n)
    x_step, v_step = forward_step(x_n, v_n, deltat)
    x_forward = x_prime(v_step)
    v_forward = v_prime(x_step)
    
    return x_n + deltat*(x_original + x_forward)/2.0, \
        v_n + deltat*(v_original + v_forward)/2.0
        
#x1, y1 = forward_step(-1, -2, 0.1)
#print (f'{x1}, {y1}')

def iterate_n(x_0, v_0, deltat, num_iter, step_type):
    x_n = x_0
    v_n = v_0
    xs = []
    vs = []
    for i in range(0, num_iter):
        x_next, v_next = step_type(x_n, v_n, deltat)
        xs.append(x_next)
        vs.append(v_next)
        x_n = x_next
        v_n = v_next
        
    return x_n, v_n, xs, vs

