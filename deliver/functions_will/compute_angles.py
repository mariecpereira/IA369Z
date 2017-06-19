# -*- encoding: utf-8 -*-
import numpy as np

def compute_angles(pivot, anterior, posterior):
    max_angle = np.pi*2

    def dotproduct(v1, v2):
        return v1[0]*v2[0] + v1[1]*v2[1]
        #return sum((a*b) for a, b in zip(v1, v2))

    def length(v):
        return np.sqrt(dotproduct(v, v))

    def angles(vectors):
        angles = np.arctan2(vectors[0], vectors[1])
        #idx = angles<0
        #angles[idx] += max_angle
        return angles

    ap, pp = anterior-pivot, posterior-pivot
    '''

    #print "ap", ap.shape, ap
    #print "pp", pp.shape, pp
    ang_t = dotproduct(ap, pp) / (length(ap) * length(pp))
    id1 = ang_t < -1
    id2 = ang_t > 1
    ang_clip = np.arccos(np.clip(ang_t,-1,1))*180/(np.pi)
    ang_clip[id2] -= 360
    ang_clip[id1] -= 360
    return ang_clip

    v1_u = ap / np.linalg.norm(ap)
    v2_u = pp / np.linalg.norm(pp)
    return np.arccos(np.clip(dotproduct(v1_u, v2_u), -1.0, 1.0))*180/(np.pi)
    '''
    ang_post, ang_ant = angles(pp), angles(ap)
    ang = ang_post - ang_ant
    idx = ang<-(3*np.pi/2.0)
    ang[idx] = (ang[idx]+(2*np.pi))
    idx = ang<0.45
    ang[idx] += max_angle
    #B = np.mod(B+(max_angle-A), max_angle)
    return 360 - ang*180/(np.pi)

