# -*- encoding: utf-8 -*-
def info_lbp(f):

    import numpy as np
    f = np.array(f, dtype='uint8')
    m,n = f.shape
    F = np.zeros(np.array(f.shape)+2, dtype='uint8')
    F[1:-1, 1:-1] = f
    g = 0
    for i, j, k in np.array([(0,0,1), (0,1,2), (0,2,4), (1,0,128), (1,2,8), (2,0,64), (2,1,32), (2,2,16)], dtype='uint8'):
        g += (F[i:i+m,j:j+n] <= f) * k
    return g

