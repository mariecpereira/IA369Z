
# coding: utf-8

# In[ ]:

def run_analysis(rootdir):  

    t1_filename = '{}/t1.nii.gz'.format(rootdir)
    print(rootdir)
    minc_filename = glob('{}/*.mnc'.format(rootdir))[0]
    print(minc_filename)
    tagfilename = glob('{}/*.tag'.format(rootdir))[0]
    brain_mask_filename = '{}/nodif_brain_mask.nii.gz'.format(rootdir)
    tag = np.loadtxt(tagfilename, skiprows=4, comments=';')


    eigvals, eigvects, T3 = loadNiftiDTI(rootdir, reorient=True)

    FA,MD = getFractionalAnisotropy(eigvals)
    FA[np.isnan(FA)] = 0
    FA[FA>1] = 1

    fissure, FA_mean = getFissureSlice(eigvals, FA)

    wFA = FA*abs(eigvects[0,0]) #weighted FA
    
    return wFA, FA, MD, fissure, eigvals, eigvects


# In[ ]:



