# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np

def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    toReturn = []
    for j in range(0,degree+1):
        toReturn = np.append(toReturn,np.power(x,j))
         
    return np.transpose(np.reshape(toReturn,(degree+1,len(x))))
