# -*- encoding: utf-8 -*-
import numpy as np
from scipy.signal import argrelextrema

def get_local_minima(arr_curve):
    xmin_loc = argrelextrema(arr_curve, np.less)
    ymin_loc = arr_curve[xmin_loc]
    min_sort = np.argsort(ymin_loc)
    n_true_min = np.sum(ymin_loc[min_sort[:4]]<80)
    val = np.sum(min_sort[:n_true_min])/(n_true_min*1.0)
    ymin_loc[min_sort[:n_true_min][min_sort[:n_true_min]>val]] = 250
    return xmin_loc[0][np.argmin(ymin_loc)]

