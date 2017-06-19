# -*- encoding: utf-8 -*-
def run_readdata(filedir):

    from glob import glob
    import nibabel as ni
    import numpy as np
    import dtimp as DTII

    file_DTI = filedir+"diffusion.nii.gz"
    file_T1 = filedir+"t1.nii.gz"
    file_mask = glob('{}/*.tag'.format(filedir))[0]
    file_bet = filedir+"nodif_brain_mask.nii.gz"
    file_L1 = filedir+"dti_L1.nii.gz"
    file_FA = filedir+"dti_FA.nii.gz"

    #Lendo T1
    t1 = ni.load(file_T1).get_data()
    shape = t1.shape

    #Lendo RAW
    vol_dti = ni.load(file_DTI).get_data()
    volume = vol_dti.transpose(3,0,2,1)#.copy()

    #Lendo matriz de registro e calculando transformada
    T = DTII.readAffineMatrix('{}reg.mat'.format(filedir))
    scale = np.diag([1,1,2,1])
    T = np.dot(T, scale)

    #Lendo eigenvalores, eigenvetores
    eigvals, eigvects, T3 = DTII.loadNiftiDTI(filedir, reorient=True)

    #Lendo mapa de FA
    FA,MD = DTII.getFractionalAnisotropy(eigvals)
    FA[np.isnan(FA)] = 0
    FA[FA>1] = 1

    #Lendo máscara segmentação cérebro
    mask_out = ni.load(file_bet).get_data().astype(bool)
    mask_out = mask_out.transpose(0,2,1)#.copy()

    #Lendo máscara corpo caloso e registrando em DTI
    tag = np.genfromtxt(file_mask, missing_values=';', skip_header = 4)
    seg_mask_t1 = DTII.createMaskSegmentationOriginal(shape, tag)
    z, y, x = seg_mask_t1.nonzero()
    pontos = np.vstack((z,y,x,np.ones(z.size)))
    T_T = np.dot(T3, np.linalg.inv(T))
    z, y, x, _ = np.round(np.dot(T_T, pontos)).astype('int')
    if np.array([z.min(), y.min(), x.min()]).min() < 0:
        return False
    seg_mask = np.zeros(FA.shape, dtype='bool')
    #z = np.clip(z, 0,255)
    #y = np.clip(y, 0,69)
    #x = np.clip(x, 0,255)
    seg_mask[z,y,x] = True

    #Encontrando fatia media no plano sagital
    fat_md, FA_mean = DTII.getFissureSlice(eigvals, FA)
    wFA = FA*abs(eigvects[0,0]) #weighted FA

    return (volume[:,:,::-1,::-1], wFA, FA, MD, fat_md, eigvals, eigvects, seg_mask_t1, seg_mask, mask_out[:,::-1,::-1])

