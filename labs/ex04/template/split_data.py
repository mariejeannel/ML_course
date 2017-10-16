# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    new = np.transpose([x,y])
    np.random.seed(seed)
    np.random.shuffle(new)
    x_new = np.transpose(new)[0]
    y_new = np.transpose(new)[1]
    lenght = len(x)
    lenght_table = lenght - 1
    index = int(np.round(ratio * len(x)))
    y_training = y_new[0:index]
    x_training = x_new[0:index]
    y_test = y_new[index:lenght_table]
    x_test=x_new[index:lenght_table]
    return x_training,y_training,x_test,y_test