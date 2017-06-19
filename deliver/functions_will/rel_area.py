# -*- encoding: utf-8 -*-
def rel_area(y_true,y_pred):

    import numpy as np

    #Função para cálculo de relação de área entre duas segmentações (Não precissam ter o mesmo tamanho).
    y_true = np.ravel(y_true)
    y_pred = np.ravel(y_pred)
    return (np.sum(y_pred)/(len(y_pred)*1.0))/(np.sum(y_true)/(len(y_true)*1.0))

