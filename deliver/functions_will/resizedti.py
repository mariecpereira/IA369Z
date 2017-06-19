# -*- encoding: utf-8 -*-
import numpy as np

def resizedti(img,shape):

    y,x = np.indices(shape)
    x /= shape[1]/img.shape[-1]
    y /= shape[0]/img.shape[-2]

    return img[y,x]

