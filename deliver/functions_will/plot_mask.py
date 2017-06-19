
# coding: utf-8

# In[ ]:

def plot_mask(im,mask,mask2,escala,mask_name):
    con_mask = np.logical_xor(mask,MM.iaero(mask))
    con_mask = np.ma.masked_where(con_mask == 0,con_mask)
    con_mask2 = np.logical_xor(mask2,MM.iaero(mask2))
    con_mask2 = np.ma.masked_where(con_mask2==0,con_mask2)
        
    plt.figure()
    plt.axis('off')
    plt.imshow(im,cmap='gray')
    plt.imshow(con_mask,cmap=mpl.cm.jet_r,interpolation='none')
    plt.imshow(con_mask2,cmap=mpl.cm.brg_r,interpolation='none')
    plt.show()

