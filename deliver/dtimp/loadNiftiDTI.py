
# coding: utf-8

# In[1]:

def align_sagittal_plane(T):
    import numpy as np

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

def loadNiftiDTI(basedir, basename='dti', reorient=False):
    from nibabel import nifti1
    import numpy as np
    import dtimp

    # ====== MAIN FUNCTION START ===========================
    # PRE-LOAD THE FIRST EIGENVALUE VOLUME TO GET HEADER PARAMS
    L = nifti1.load('{}/{}_L1.nii.gz'.format(basedir, basename))
    s,m,n = L.get_data().shape

    # LOAD AND BUILD EIGENVALUES VOLUME
    evl = [L.get_data()]
    evl.append(nifti1.load('{}/{}_L2.nii.gz'.format(basedir, basename)).get_data())
    evl.append(nifti1.load('{}/{}_L3.nii.gz'.format(basedir, basename)).get_data())
    evl = np.array(evl)
    evl[evl<0] = 0

    # LOAD AND BUILD EIGENVECTORS VOLUME
    evt = [nifti1.load('{}/{}_V1.nii.gz'.format(basedir, basename)).get_data()]
    evt.append(nifti1.load('{}/{}_V2.nii.gz'.format(basedir, basename)).get_data())
    evt.append(nifti1.load('{}/{}_V3.nii.gz'.format(basedir, basename)).get_data())
    evt = np.array(evt).transpose(0,4,1,2,3)

    T = np.diag(np.ones(4))
    if reorient:
        # GET QFORM AFFINE MATRIX (see Nifti and nibabel specifications)
        T = L.get_header().get_qform()

        # COMPUTE ROTATION MATRIX TO ALIGN SAGITTAL PLANE
        R = align_sagittal_plane(T)
        evl, evt, T = dtimp.rotateDTI(evl, evt, R)

    return (evl, evt, T)

# In[ ]:



