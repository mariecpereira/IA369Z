# -*- encoding: utf-8 -*-
def metrics(y_true,y_pred):

    import numpy as np
    from sklearn.metrics import recall_score, precision_score, jaccard_similarity_score, confusion_matrix

    #Função para extração de valores métricos, retornando Sensibilidade, Especificidade, Recall, Precision, Jaccard, Dice e Area.

    y_true = np.ravel(y_true)
    y_pred = np.ravel(y_pred)

    MC = confusion_matrix(y_true,y_pred,labels=(True,False))
    TP, FP, FN, TN = MC[0,0], MC[1,0], MC[0,1], MC[1,1]

    Sensi = TP/(1.0*(TP+FN))
    Speci = TN/(1.0*(TN+FP))
    Recall = TP/(1.0*(np.sum(y_true)))
    Precision = TP/(1.0*(np.sum(y_pred)))
    Jaccard = TP/(1.0*(TP+FP+FN))
    Dice = (2*TP)/(1.0*(2*TP+FP+FN))
    Area = (TP+FP)/(1.0*(TP+FN))

    return Sensi, Speci, Recall, Precision, Jaccard, Dice, Area

