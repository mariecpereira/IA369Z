# -*- encoding: utf-8 -*-
def extract_feature_dif(img, mask_1, mask_0=[], mask_2=[], mask_3=[], dim_prof=0):

    import numpy as np

    #Função de leitura da imagem e máscaras, e retorna array de pixel como atributo

    n = img.shape[dim_prof]
    t1 = img[mask_1].size/n
    t0 = img[mask_0].size/n
    t2 = img[mask_2].size/n
    t3 = img[mask_3].size/n

    ones = np.ones((t1,1))
    eval1 = img[mask_1].reshape(n,-1).T

    ftr1_coord = np.nonzero(mask_1[0])
    ftr1_coord = np.array((ftr1_coord[0],ftr1_coord[1])).T
    atr_slice = np.concatenate((eval1,ftr1_coord), axis=1)
    atr_slice = np.concatenate((atr_slice,ones), axis=1)

    if mask_0!=[]:
        zeros = np.zeros((t0,1))
        eval0 = img[mask_0].reshape(n,-1).T

        ftr0_coord = np.nonzero(mask_0[0])
        ftr0_coord = np.array((ftr0_coord[0],ftr0_coord[1])).T
        atr_slice0 = np.concatenate((eval0,ftr0_coord), axis=1)
        atr0 = np.concatenate((atr_slice0,zeros), axis=1)
        atr_slice = np.vstack([atr0,atr_slice])

    if mask_2!=[]:
        twos = np.ones((t2,1))*2
        eval2 = img[mask_2].reshape(n,-1).T

        ftr2_coord = np.nonzero(mask_2[0])
        ftr2_coord = np.array((ftr2_coord[0],ftr2_coord[1])).T
        atr_slice2 = np.concatenate((eval2,ftr2_coord), axis=1)
        atr2 = np.concatenate((atr_slice2,twos), axis=1)
        atr_slice = np.vstack([atr_slice,atr2])

    if mask_3!=[]:
        threes = np.ones((t3,1))*3
        eval3 = img[mask_3].reshape(n,-1).T

        ftr3_coord = np.nonzero(mask_3[0])
        ftr3_coord = np.array((ftr3_coord[0],ftr3_coord[1])).T
        atr_slice3 = np.concatenate((eval3,ftr3_coord), axis=1)
        atr3 = np.concatenate((atr_slice3,threes), axis=1)
        atr_slice = np.vstack([atr_slice,atr3])

    return atr_slice

