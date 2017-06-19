# -*- encoding: utf-8 -*-
import ia870 as MM
import numpy as np
import morph as mor

def dynamics2(img,n,dyn):

    disk = MM.iasedisk(1,'2D','CITY-BLOCK','FLAT')
    minDyn = mor.mmregmin(img,disk,dyn)
    minLab = MM.ialabel(MM.iaregmin(img,disk),disk)
    minLis = np.unique(minDyn)
    #minLis = array(np.nonzero(iahistogram(minDyn)))

    #minFinal = zeros(minDyn.shape)

    cont = 0
    i = 1
    while cont<n:
        teste = minLis[-i]
        y,x = np.nonzero(minDyn==teste)
        reg = np.unique(minLab[y,x])
        #reg, = array(nonzero(iahistogram(minLab[y,x])))
        #for k in reg:
        #    minFinal[minLab==k]=k
        cont += reg.shape[0]
        i += 1

    minFinal = (minDyn>=teste)

    #print cont
    #print i

    return minFinal

