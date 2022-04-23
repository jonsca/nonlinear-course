# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 04:58:55 2022

@author: Jonathan
"""

import odesolvers as ods
import matplotlib.pyplot as p

x_5, v_5, _, _ = ods.iterate_n(-1,-2, 0.1, 5, ods.combined_step)

#print(f"{x_5},{v_5}")

_, _, x_500, v_500 = ods.iterate_n(-1, -2, 0.01, 500, ods.combined_step)
_, _, x_5000, v_5000 = ods.iterate_n(-1, -2, 0.01, 5000, ods.combined_step)

p.plot(x_500, v_500, '.')


