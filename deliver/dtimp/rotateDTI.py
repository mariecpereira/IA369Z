
# coding: utf-8

# In[ ]:

def rotateDTI(evl, evt, R):
    import numpy as np 


    s,m,n = evl[0].shape

    # ====== DETERMINE TARGET DOMAIN SIZE AND A TRANSLATION TO FIT THE ROTATED IMAGE =======
    # VERTICES FROM THE CUBE DEFINING THE ORIGINAL VOLUME
    cube = np.array([[0,0,0,1],
                     [0,0,n,1],
                     [0,m,n,1],
                     [0,m,0,1],
                     [s,m,0,1],
                     [s,0,0,1],
                     [s,0,n,1],
                     [s,m,n,1]]).transpose()

    # COMPUTE THE FIT TRANSLATION AND COMBINE WITH THE ROTATION
    cube = np.dot(R,cube)
    t = -cube.min(axis=1)
    Tr = np.diag(np.ones(4, dtype='float'))
    Tr[:3,3] = t[:3]
    T = np.dot(Tr,R)

    # DEFINE THE TARGET DOMAIN
    cube = cube + t.reshape(4,1)
    domain = np.ceil(cube.max(axis=1))[:3].astype('int')

    # === TRANSFORMATION ===
    invT = np.linalg.inv(T)
    N = domain.prod()

    # GET INDICES IN TARGET SPACE
    points = np.array(np.indices(domain)).reshape(3,N)
    points = np.vstack((points, np.ones(N)))

    # COMPUTE POINT COORDINATES WITH NEAREST NEIGHBOR INTERPOLATION
    points = np.dot(invT, points)[:3]
    points = np.round(points).astype('int')
    out_of_space = np.logical_or(points<0, points>=np.array([s,m,n]).reshape(3,1)).max(axis=0)
    points[:,out_of_space] = 0
    z,y,x = points

    # APPLY TRANSFORMATION TO THE EIGENVALUES VOLUME
    eigenvals = evl[:,z,y,x].copy()
    eigenvals[:,out_of_space] = 0
    eigenvals.shape = (3,) + tuple(domain)

    # APPLY ROTATION TO THE EIGENVECTORS
    evt = evt.copy()
    evt.shape = (3,3,s*m*n)
    for i in xrange(3):
        evt[i] = np.dot(R[:3,:3],evt[i])
    evt.shape = (3,3,s,m,n)

    # APPLY TRANSFORMATION TO THE EIGENVECTORS VOLUME
    eigenvects = evt[:,:,z,y,x]
    eigenvects[:,:,out_of_space] = 0
    eigenvects.shape = (3,3) + tuple(domain)

    return (eigenvals, eigenvects, T)


# In[ ]:



