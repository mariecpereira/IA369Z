
# coding: utf-8

# In[1]:

def getFissureSlice(eigvals, FA):
    import numpy as np

    MASK = (eigvals[0]>0)
    MASKcount = MASK.sum(axis=2).sum(axis=1)
    FAmean = FA.mean(axis=2).mean(axis=1)
    FAmean[MASKcount<=0.90*MASKcount.max()] = 1
    return (np.argmin(FAmean), FAmean)


# In[ ]:



