
# coding: utf-8

# In[ ]:

def getFractionalAnisotropy(eigvals):
    import numpy as np
    MD = eigvals.mean(axis=0)
    FA = np.sqrt(3*((eigvals-MD)**2).sum(axis=0)) / np.sqrt(2*(eigvals**2).sum(axis=0))
    return (FA,MD)


# In[ ]:



