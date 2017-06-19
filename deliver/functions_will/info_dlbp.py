# -*- encoding: utf-8 -*-
def info_dlbp(f):

    import numpy as np

    f = np.array(f, dtype='uint8')
    h,w = f.shape
    F = np.zeros(np.array(f.shape)+2, dtype='uint8')
    F[1:-1, 1:-1] = f
    g = 0
    for i, j, k, l in np.array([(0,2,1,2), (1,2,2,4), (2,2,4,8), (2,1,8,16)], dtype='uint8'):
        g += (F[i:i+h,j:j+w] >= f)*((F[i:i+h,j:j+w]+4) - f)*k+(abs(F[i:i+h,j:j+w]-f) >= abs(F[i:i+h,j:j+w]+4-f))*l
    return g

