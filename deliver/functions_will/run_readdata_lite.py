# -*- encoding: utf-8 -*-
def run_readdata_lite(filedir):

    from glob import glob
    import nibabel as ni
    import numpy as np
    import dtimp as DTII

    file_DTI = filedir+"/diffusion.nii.gz"

    #Lendo RAW
    vol_dti = ni.load(file_DTI).get_data()
    volume = vol_dti.transpose(3,0,2,1)#.copy()

    #Lendo eigenvalores, eigenvetores
    eigvals, eigvects, T3 = DTII.loadNiftiDTI(filedir, reorient=True)

    #Lendo mapa de FA
    FA,MD = DTII.getFractionalAnisotropy(eigvals)
    FA[np.isnan(FA)] = 0
    FA[FA>1] = 1

    #Encontrando fatia media no plano sagital
    fat_md, FA_mean = DTII.getFissureSlice(eigvals, FA)
    wFA = FA*abs(eigvects[0,0]) #weighted FA

    return volume[:,:,::-1,::-1], wFA, FA, MD, fat_md, eigvals, eigvects

