# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    #w = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(tx),tx)),np.transpose(tx)),y)
    w = np.linalg.solve(np.dot(np.transpose(tx),tx),np.dot(np.transpose(tx),y))
    error = y - np.dot(tx,w)
    return w,error
