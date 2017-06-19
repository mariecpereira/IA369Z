# -*- encoding: utf-8 -*-
def dim_mask2dim_img(shape_img,mask):

    import numpy as np

    #Função para dar à máscara a mesma profundidade do que a imagem de entrada

    mask_temp = np.empty((shape_img), dtype=bool)
    mask_temp[:] = np.expand_dims(mask, axis=0)
    return mask_temp

