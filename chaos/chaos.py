# -*- coding: utf-8 -*-
"""
@author: Sandeepan
"""

from configurator import configurator as cfgr
SIGMA, BETA, RHO, ALPHA, GAMMA, DT, MSG_FILE = cfgr('setup.cfg')

def lorenz(x, y, z):
    """
    Test usage:
    lorenz(x_position, y_position, z_position)
    """
    sigma=SIGMA
    beta=BETA
    rho=RHO

    x_dot = sigma*(y-x)
    y_dot = x*(rho-z)-y
    z_dot = x*y-beta*z

    return x_dot, y_dot, z_dot

def chen(x, y, z, alpha=ALPHA, beta=BETA, gamma=GAMMA) :

    x_dot = alpha * (y - x)
    y_dot = x * (gamma - alpha) - (x * z) + (gamma * y)
    z_dot = (x * y) - (beta * z)

    return x_dot, y_dot, z_dot