# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    return np.linalg.solve(np.dot(np.transpose(tx),tx)+((2*len(y)*lambda_)*np.identity(tx.shape[1])),np.dot(np.transpose(tx),y))

