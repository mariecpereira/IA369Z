# -*- encoding: utf-8 -*-
import numpy as np
import ia870 as MM

def hausdorff(mask_a,mask_b):
    bnd_a = np.nonzero(np.logical_xor(MM.iaero(mask_a),mask_a))
    bnd_b = np.nonzero(np.logical_xor(MM.iaero(mask_b),mask_b))
    dist_lst = []
    for i in range(len(bnd_a[0])):
        dist_min = 1000.0
        for j in range(len(bnd_b[0])):
            dist = np.linalg.norm((bnd_a[0][i]-bnd_b[0][j],bnd_a[1][i]-bnd_b[1][j]))
            if dist_min > dist:
                dist_min = dist
        dist_lst.append(dist_min)
    for i in range(len(bnd_b[0])):
        dist_min = 1000.0
        for j in range(len(bnd_a[0])):
            dist = np.linalg.norm((bnd_b[0][i]-bnd_a[0][j],bnd_b[1][i]-bnd_a[1][j]))
            if dist_min > dist:
                dist_min = dist
        dist_lst.append(dist_min)
    return np.max(dist_lst)

