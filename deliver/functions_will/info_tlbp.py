# -*- encoding: utf-8 -*-
def info_tlbp(f):

    import numpy as np

    f = np.array(f, dtype='uint8')
    h,w = f.shape
    F = np.zeros(np.array(f.shape)+2, dtype='uint8')
    F[1:-1, 1:-1] = f
    g = 0
    for i, j, m, n, k in np.array([(0,0,0,1,1), (0,1,0,2,2), (0,2,1,2,4), (1,2,2,2,128), (2,2,2,1,8),
                                   (2,1,2,0,64), (2,0,1,0,32), (1,0,0,0,16)], dtype='uint8'):
        g += (F[i:i+h,j:j+w] <= F[m:m+h,n:n+w]) * k
    return g

