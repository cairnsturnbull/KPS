"""
evaluating initial conditions
"""
import numpy as np

E = 1.0e+52
eta = 50
UNIT_DENSITY = 1.673e-24
UNIT_VELOCITY = 2.998e+10
UNIT_LENGTH = 3.0e+10
CONST_c = UNIT_VELOCITY
CONST_mp = 1.6726219e-24

unit_pressure = UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
unit_volume = (4.0/3.0) * np.pi * UNIT_LENGTH * UNIT_LENGTH * UNIT_LENGTH

M_0 = E / (eta * CONST_c * CONST_c)
rho_0 = (M_0 / unit_volume)#/CONST_mp

e = (E * (1-1/eta)) / unit_volume
p_0 = (e / 3.0)#/unit_pressure

print(rho_0, p_0)
