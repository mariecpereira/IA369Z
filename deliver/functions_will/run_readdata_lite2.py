# -*- encoding: utf-8 -*-
def run_readdata_lite2(filedir):

    from glob import glob
    import nibabel as ni
    import numpy as np
    import dtimp as DTII
    from scipy import misc
    import Image
    import homewilliam as HW

    file_DTI = filedir+"/diffusion.nii.gz"
    file_bet = filedir+"/nodif_brain_mask.nii.gz"
    file_msk = HW.find_file(filedir+"/mask_AF.png")

    #Lendo RAW
    vol_dti = ni.load(file_DTI).get_data()
    volume = vol_dti.transpose(3,0,2,1)#.copy()

    #Lendo eigenvalores, eigenvetores
    eigvals, eigvects, T3 = DTII.loadNiftiDTI(filedir, reorient=True)

    #Lendo mapa de FA
    FA,MD = DTII.getFractionalAnisotropy(eigvals)
    FA[np.isnan(FA)] = 0
    FA[FA>1] = 1

    #Lendo máscara segmentação cérebro
    mask_out = ni.load(file_bet).get_data().astype(bool)
    mask_out = mask_out.transpose(0,2,1)#.copy()

    #Encontrando fatia media no plano sagital
    fat_md, FA_mean = DTII.getFissureSlice(eigvals, FA)
    wFA = FA*abs(eigvects[0,0]) #weighted FA

    #Máscara semi-automática
    escala = [wFA[fat_md].shape[-2],wFA[fat_md].shape[-1]]
    mask_DTI = HW.pil_array(Image.open(file_msk))

    mask_DTI = np.array(mask_DTI).astype('bool')
    mask_DTI = mask_DTI[0,:,:]
    mask_sem = misc.imresize(mask_DTI,escala).astype(bool)

    return volume[:,:,::-1,::-1], wFA, fat_md, mask_sem, mask_out[:,::-1,::-1]

