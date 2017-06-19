# -*- encoding: utf-8 -*-
def extract_feature_pixel(img, mask_1, mask_0=[], mask_2=[], mask_3=[], mask_4=[], mask_5=[], dim_prof=0):

    import numpy as np

    #Função de leitura da imagem e máscaras, e retorna array de pixel como atributo

    n = img.shape[dim_prof]
    t1 = img[mask_1].size/n
    t0 = img[mask_0].size/n
    t2 = img[mask_2].size/n
    t3 = img[mask_3].size/n
    t4 = img[mask_4].size/n
    t5 = img[mask_5].size/n

    ones = np.ones((t1,1))
    eval1 = img[mask_1].reshape(n,-1).T
    atr_slice = np.concatenate((eval1,ones), axis=1)

    if mask_0!=[]:
        zeros = np.zeros((t0,1))
        eval0 = img[mask_0].reshape(n,-1).T
        atr0 = np.concatenate((eval0,zeros), axis=1)
        atr_slice = np.vstack([atr0,atr_slice])

    if mask_2!=[]:
        twos = np.ones((t2,1))*2
        eval2 = img[mask_2].reshape(n,-1).T
        atr2 = np.concatenate((eval2,twos), axis=1)
        atr_slice = np.vstack([atr_slice,atr2])

    if mask_3!=[]:
        threes = np.ones((t3,1))*3
        eval3 = img[mask_3].reshape(n,-1).T
        atr3 = np.concatenate((eval3,threes), axis=1)
        atr_slice = np.vstack([atr_slice,atr3])

    if mask_4!=[]:
        fours = np.ones((t4,1))*4
        eval4 = img[mask_4].reshape(n,-1).T
        atr4 = np.concatenate((eval4,fours), axis=1)
        atr_slice = np.vstack([atr_slice,atr4])

    if mask_5!=[]:
        fives = np.ones((t5,1))*5
        eval5 = img[mask_5].reshape(n,-1).T
        atr5 = np.concatenate((eval5,fives), axis=1)
        atr_slice = np.vstack([atr_slice,atr5])

    return atr_slice

