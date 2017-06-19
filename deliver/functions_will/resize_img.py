# -*- encoding: utf-8 -*-
import numpy as np

def resize_img(a,scale):
    new_a = np.zeros((np.array(a.shape)*scale))
    for i in xrange(scale):
        for j in xrange(scale):
            new_a[i::scale,j::scale]=a
    return new_a

