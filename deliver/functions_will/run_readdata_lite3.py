# -*- encoding: utf-8 -*-
def run_readdata_lite3(filedir):

    from glob import glob
    from scipy import misc
    import nibabel as ni
    import numpy as np
    import dtimp as DTII
    import homewilliam as HW
    import Image

    file_msk = HW.find_file(filedir+"/mask_AF.png")

    #Lendo eigenvalores, eigenvetores
    eigvals, eigvects, T3 = DTII.loadNiftiDTI(filedir, reorient=True)

    #Lendo mapa de FA
    FA,MD = DTII.getFractionalAnisotropy(eigvals)
    FA[np.isnan(FA)] = 0
    FA[FA>1] = 1

    #Encontrando fatia media no plano sagital
    fat_md, FA_mean = DTII.getFissureSlice(eigvals, FA)
    wFA = FA*abs(eigvects[0,0]) #weighted FA

    #Máscara semi-automática
    escala = [wFA[fat_md].shape[-2],wFA[fat_md].shape[-1]]
    mask_DTI = HW.pil_array(Image.open(file_msk))

    mask_DTI = np.array(mask_DTI).astype('bool')
    mask_DTI = mask_DTI[0,:,:]
    mask_sem = misc.imresize(mask_DTI,escala).astype(bool)

    return (wFA, FA, fat_md, eigvals, eigvects, mask_sem)

