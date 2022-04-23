# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 05:01:53 2022

@author: Jonathan
"""

import odesolvers as ods
import matplotlib.pyplot as p

x2, y2, _, _ = ods.iterate_n(-1, -2, 0.1, 1, ods.forward_step)

#print(f'{x2},{y2}')

x_hw, y_hw, _, _ = ods.iterate_n(-1, -2, 0.1, 5, ods.forward_step)

#print(f'{x_hw}, {y_hw}')

x_hw, y_hw, _, _ = ods.iterate_n(-1, -2, 0.1, 5, ods.backward_step)
print(f'{x_hw}, {y_hw}')


_, _, xs1, vs1 = ods.iterate_n(-1, -2, 0.1, 200, ods.forward_step)
_, _, xs2, vs2 = ods.iterate_n(-1, -2, 0.11, 200, ods.forward_step)



_, _, xs1, vs1 = ods.iterate_n(-1, -2, 0.1, 200, ods.backward_step)
_, _, xs2, vs2 = ods.iterate_n(-1, -2, 0.11, 200, ods.backward_step)

p.plot(xs1, vs1, xs2, vs2)

_, _, xs1, vs1 = ods.iterate_n(-1, -2, 0.1, 50, ods.forward_step)
_, _, xs2, vs2 = ods.iterate_n(-1, -2, 0.1, 50, ods.backward_step)


