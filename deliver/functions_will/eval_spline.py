# -*- encoding: utf-8 -*-
import numpy as np
import scipy.interpolate as spline

def eval_spline(tck, t):
    y, x = spline.splev(t,tck)
    return np.vstack((y,x))

