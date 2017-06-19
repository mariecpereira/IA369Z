
# coding: utf-8

# In[1]:

def loadNiftiDTI(basedir, basename='dti', reorient=False):
    from nibabel import nifti1


    # ====== MAIN FUNCTION START ===========================
    # PRE-LOAD THE FIRST EIGENVALUE VOLUME TO GET HEADER PARAMS
    L = ni.load('{}/{}_L1.nii.gz'.format(basedir, basename))
    s,m,n = L.get_data().shape

    # LOAD AND BUILD EIGENVALUES VOLUME
    evl = [L.get_data()]
    evl.append(ni.load('{}/{}_L2.nii.gz'.format(basedir, basename)).get_data())
    evl.append(ni.load('{}/{}_L3.nii.gz'.format(basedir, basename)).get_data())
    evl = np.array(evl)
    evl[evl<0] = 0

    # LOAD AND BUILD EIGENVECTORS VOLUME
    evt = [ni.load('{}/{}_V1.nii.gz'.format(basedir, basename)).get_data()]
    evt.append(ni.load('{}/{}_V2.nii.gz'.format(basedir, basename)).get_data())
    evt.append(ni.load('{}/{}_V3.nii.gz'.format(basedir, basename)).get_data())
    evt = np.array(evt).transpose(0,4,1,2,3)

    T = np.diag(np.ones(4))
    if reorient:
        # GET QFORM AFFINE MATRIX (see Nifti and nibabel specifications)
        T = L.get_header().get_qform()

        # COMPUTE ROTATION MATRIX TO ALIGN SAGITTAL PLANE
        R = alignSagittalPlane(T)
        evl, evt, T = rotateDTI(evl, evt, R)

    return (evl, evt, T)


# In[ ]:



