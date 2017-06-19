# -*- encoding: utf-8 -*-
import numpy as np
import ia870 as MM
#import ia636 as ia
import scipy.interpolate as spline
import scipy.misc as misc
import scipy.spatial.distance as distance

def profile_metrics(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))

    return np.sqrt(np.sum((prof_ref - prof_seg_shift)**2,axis=1)/(prof_ref.shape[1]))

def kull_leib(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    return np.sum(prof_ref*np.log(prof_ref/prof_seg_shift),axis=1)

def cross_entr(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    return np.sum(prof_ref*np.log(1/prof_seg_shift),axis=1)

def srf(prof_ref,prof_seg):
    prof_ref = prof_ref[1:]
    prof_seg = prof_seg[1:]
    N_ref = prof_ref.shape[1]
    N_seg = prof_seg.shape[1]
    N_cur = prof_seg.shape[0]
    fft_ref = np.abs(np.fft.fft(prof_ref,axis=1))[:,:(N_ref/2+1)]
    fft_seg = np.abs(np.fft.fft(prof_seg,axis=1))[:,:(N_seg/2+1)]
    norm = 2
    DM = np.power(np.sum(abs(fft_ref - fft_seg)**norm,axis=1)/(fft_ref.shape[1]),1/(1.0*norm))
    C_ref = np.sum(np.amax(prof_ref,axis=1)-np.amin(prof_ref,axis=1))/(N_ref)
    C_seg = np.sum(np.amax(prof_seg,axis=1)-np.amin(prof_seg,axis=1))/(N_seg)
    return np.sum(DM)/(N_cur*(C_ref+C_seg))

def mink(prof_ref,prof_seg,norm=2):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    return np.power(np.sum(abs(prof_ref - prof_seg_shift)**norm,axis=1)/(prof_ref.shape[1]),1/(1.0*norm))

def hid(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    return np.sum(np.amin((prof_ref,prof_seg_shift),axis=0),axis=1)/prof_ref.shape[1]

def cosine(prof_ref,prof_seg):
    dif_curv = []
    res_cum = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    for linha in range(prof_ref.shape[0]):
        res_cum.append(distance.cosine(prof_ref[linha],prof_seg_shift[linha]))
    return res_cum

def x_statistics(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    m = (prof_ref+prof_seg_shift)/2.0
    return np.sum(((prof_ref - prof_seg_shift)**2)/m,axis=1)

def bend(prof_ref,prof_seg):
    dif_curv = []
    for shift in range(prof_seg.shape[1]):
        dif_curv.append(np.abs(np.sum((prof_ref[0] - np.roll(prof_seg[0],shift))**2)))
    prof_seg_shift = np.apply_along_axis(np.roll, 1, prof_seg, np.argmin(dif_curv))
    return np.trapz(prof_seg_shift**2,axis=1)/(1.0*np.trapz(prof_ref**2,axis=1))

