# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np

<<<<<<< HEAD
def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    toReturn = []
    for j in range(0,degree+1):
        toReturn = np.append(toReturn,np.power(x,j))
        
       
    return np.transpose(np.reshape(toReturn,(degree+1,len(x))))
=======

def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    raise NotImplementedError
>>>>>>> upstream/master
