# -*- encoding: utf-8 -*-
import numpy as np

def rmse(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))

    return np.sqrt(np.sum((prof_ref - prof_seg_shift)**2,axis=1)/(prof_ref.shape[1]))

