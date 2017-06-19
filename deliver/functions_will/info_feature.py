# -*- encoding: utf-8 -*-
import ia870 as MM
import numpy as np
import morph as mor

def info_feature(vec_tt):

    print "Shape vec_tt: ", vec_tt[:,:-3].shape
    print "**************Rótulos**************"
    all_lab = np.unique(vec_tt[:,-3])
    for lab in all_lab:
        in_lab = np.count_nonzero(vec_tt[:,-3]==lab)
        print "No samples label ", lab, ": ", in_lab
    print "*************Pacientes*************"
    all_lab = np.unique(vec_tt[:,-2])
    for lab in all_lab:
        in_lab = np.count_nonzero(vec_tt[:,-2]==lab)
        print "No samples subject ", lab, ": ", in_lab
    print "**************Slices***************"
    all_lab = np.unique(vec_tt[:,-1])
    for lab in all_lab:
        in_lab = np.count_nonzero(vec_tt[:,-1]==lab)
        print "No samples slice ", lab, ": ", in_lab

    return

