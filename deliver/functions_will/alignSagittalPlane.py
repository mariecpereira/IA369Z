
# coding: utf-8

# In[1]:

def alignSagittalPlane(T):

    # CANONICAL BASE (i,j,k) (HOMOGENEOUS COORDINATES)
    c = np.array(
        [[0,1,0,0],
         [0,0,1,0],
         [0,0,0,1],
         [1,1,1,1]])

    # FIND BASE V
    V_ = np.dot(T,c)
    V_ = V_[:3,1:] - V_[:3,0].reshape(3,1)

    V = np.zeros((3,3))
    V[np.arange(3),np.argmax(np.abs(V_), axis=1)] = 1
    V_[V_==0] = 1
    V = V * (V_/np.abs(V_))

    # DESIRED BASE W
    W = np.array([[1,0,0],
                  [0,0,-1],
                  [0,-1,0]])

    R = np.dot(np.linalg.inv(W), V)
    r = np.diag(np.ones(4))
    r[:3,:3] = R
    return r


# In[ ]:



