
# coding: utf-8

# In[1]:

def ROI2D(segmentation, edge=0):
    import numpy as np
    h,w = segmentation.shape
    y,x = segmentation.nonzero()
    y0,y1 = max(0, y.min()-edge), min(h, y.max()+edge+1)
    x0,x1 = max(0, x.min()-edge), min(w, x.max()+edge+1)
    return (y0,y1,x0,x1)


# In[ ]:



