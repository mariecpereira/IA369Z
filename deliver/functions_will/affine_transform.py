# -*- encoding: utf-8 -*-
import ia870 as MM
import numpy as np
import morph as mor

def affine_transform(f, T, destshape=None, interpol='NEAREST'):

    #Função para aplicar affine transformation T

    if len(f.shape)==2:
        return affine_transform_2(f, T, destshape, interpol)
    elif len(f.shape)==3:
        return affine_transform_3(f, T, destshape, interpol)
    else:
        raise ValueError, 'This operation is only available of 2D or 3D arrays.'

def affine_transform_2(f, T, destshape, interpol):

    if T.ndim != 2 or T.shape[0] != T.shape[1] or T.shape[0] != 3:
        raise ValueError, 'T must be a 3x3 matrix'

    if len(f.shape)!=2:
        raise ValueError, 'f must be a bidimensional array'

    h,w = f.shape

    if destshape is None:
        corners = np.array([[0,0,1],[h,0,1],[0,w,1],[h,w,1]]).transpose()
        corners = np.dot(T,corners)
        tmp = corners.min(axis=1)[:2]
        domainC = -tmp + corners.max(axis=1)[:2]
        domainI = np.ceil(domainC)
        t = -tmp + (domainI - domainC)/2.0
        domain = domainI.astype('int')
    else:
        domain = destshape.astype('float')
        t = (domain - np.array(f.shape, dtype='float'))/2.0
        domain = domain.astype('int')

    translation = np.diag(np.ones(3, dtype='float32'))
    translation[:2,2] = t
    T = np.dot(translation,T)
    n = domain.prod()

    # get indices in target space
    points = np.array(np.indices(domain)).reshape(2,n)
    points = np.vstack((points, np.ones(n))).astype('float32')

    invT = np.linalg.inv(T.astype('float32'))
    points = np.dot(invT, points)[:2].copy()
    out_of_space = np.logical_or(points<0, points>(np.array(f.shape).reshape(2,1)-1)).max(axis=0)
    points[:,out_of_space] = 0

    if interpol=='NEAREST':
        y,x = np.round(points).astype('int')
        g = f[y, x]
    else:
        g = bilinear_interpolation(f, points).astype(f.dtype)
    g[out_of_space] = 0
    return g.reshape(domain)

def calculate_domain(shape, T):

    d,h,w = shape
    corners = np.array([[0,0,0,1],[0,h,0,1],[0,0,w,1],[0,h,w,1],
                        [d,0,0,1],[d,h,0,1],[d,0,w,1],[d,h,w,1]]).transpose()
    corners = np.dot(T,corners)
    tmp = corners.min(axis=1)[:3]
    t = np.diag(np.ones(4))
    t[:3,3] = -tmp
    T = np.dot(t, T)
    domain = np.ceil(-tmp + corners.max(axis=1)[:3]).astype('int')
    return (domain, T)

def affine_transform_3(f, T, destshape, interpol):

    if T.ndim != 2 or T.shape[0] != T.shape[1] or T.shape[0] != 4:
        raise ValueError, 'T must be a 4x4 matrix'

    if len(f.shape)!=3:
        raise ValueError, 'f must be a tridimensional array'

    f = f.astype('float32')
    d,h,w = f.shape

    if destshape is None:
        domain, T = calculate_domain((d,h,w), T)
    else:
        domain = destshape

    invT = np.linalg.inv(T.astype('float32'))

    n = domain[0]*domain[1]*domain[2]

    # get indices in target space
    points = np.array(np.indices(domain)).reshape(3,n)
    points = np.vstack((points, np.ones(n))).astype('float32')

    points = np.dot(invT, points)[:3]
    out_of_space = np.logical_or(points<0, points>(np.array(f.shape).reshape(3,1)-1)).max(axis=0)
    points[:,out_of_space] = 0

    if interpol=='NEAREST':
        points = np.round(points).astype('int')
        g = f[points[0], points[1], points[2]]
    else:
        g = trilinear_interpolation(f, points)
    g[out_of_space] = 0
    return g.reshape(domain)

