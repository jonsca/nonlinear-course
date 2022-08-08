# -*- coding: utf-8 -*-
"""
odesolvers.py
Module of functions for numerical integration of the
simple harmonic oscillator equations

Written by JScabich for the Complexity Explorer class
"Nonlinear Dynamics: Mathematical and Computational Approaches"

Equations modeled:
x' = v
v' = -x(k/m) - beta*v

Being able to plug a v_prime or x_prime into the step functions would 
be a logical next step to improve this code.  For now, they are hardcoded into
the forward_step, backward_step, and combined_step functions.

Type suggestions for Python would be another step to take with this code

License: MIT
"""

def x_prime(v):
    '''
    Helper function to define x' in the simple harmonic oscillator
    equations.  Able to be modified to solve different equations without 
    having to drastically change the integration code

    Parameters: v (velocity)

    Returns: x'
    '''
    return v

def v_prime(x, k=2, m=0.5, beta=0, v=0):
    '''
    Helper function to define v' in the simple harmonic oscillator 
    equations.  Able to be modified to solve a different set of equations
    without having to drastically change the integration code
    since there are default parameters

    Parameters: 
        x(position)
        k(damping constant)
        m(mass) default 0.5
        beta(friction) default 0
        v(velocity) default 0

    Returns: v'
    ''' 
    return -x*(k/m) - beta*v

def forward_step(x_n, v_n, deltat):
    '''
    In solving the differential equation, we can do a simple 
    delta t step via Euler's method

    x_n+1 = x(n)'*deltat
    v_n+1 = v(n)'*deltat

    Parameters:
        x_n(current value of x)
        v_n(current value of v)
        deltat(time step)

    Returns tuple (x_n+1, v_n+1)

    Designed to be plugged into iterate_n
    '''
    return x_n + deltat*x_prime(v_n), v_n + deltat*v_prime(x_n)

def backward_step(x_n, v_n, deltat):
    '''
    In solving the differential equation, we can take a forward step and
    then evaluate the differentials at that time step and use them to 
    calculate the previous delta x for x_n

    x_n+1 = x_n + deltat*(x_n+1)'
    v_n+1 = v_n + deltat*(v_n+1)' 

    Parameters:
        x_n(current value of x)
        v_n(current value of v)
        deltat(time step)

    Returns: tuple (x_n+1, v_n+1)

    Designed to be plugged into iterate_n
    '''
    
    x_step, v_step = forward_step(x_n, v_n, deltat)
    return x_n + deltat*x_prime(v_step), v_n + deltat*v_prime(x_step)

def combined_step(x_n, v_n, deltat):
    '''
    In solving the differential equation, we can take a forward
    step and average that with a regular step

    Parameters:
        x_n(current value of x)
        v_n(current value of v)
        deltat(time step)

    Returns: tuple (x_n+1, v_n+1)

    Requires: forward_step function
    
    Designed to be plugged into iterate_n
    '''
    
    x_original = x_prime(v_n)
    v_original = v_prime(x_n)
    x_step, v_step = forward_step(x_n, v_n, deltat)
    x_forward = x_prime(v_step)
    v_forward = v_prime(x_step)
    
    return x_n + deltat*(x_original + x_forward)/2.0, \
        v_n + deltat*(v_original + v_forward)/2.0
        
def iterate_n(x_0, v_0, deltat, num_iter, step_type):
    '''Perform n iterations to solve the differential equations
       Returns the nth values and the entire series by tuple
    
    Parameters:
        x_0 (initial value for x)
        v_0 (initial value for v)
        deltat (time step)
        num_iter (number of iterations to process)
        step_type:
            one of:
                forward_step
                backward_step
                combined_step
    
    Returns: tuple (x_n, v_n, xs, vs)
        x_n (value at iteration n)
        v_n (value at iteration n)
        xs (function values of x)
        vs (function values of v)

    '''
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

