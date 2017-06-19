
# coding: utf-8

# In[ ]:

def corpusCallosumParcellationGeometric (segmentation, scheme = 'HOFER'):
    import numpy as np 

    SCHEMES = ['HOFER', 'WITELSON']
    scheme = scheme.upper()
    if not scheme in SCHEMES:
        raise Exception('Unknown scheme!')

    def coef_linear (a, p):
        return p[0]-a*p[1] 

    def predicty(x, a, b):
        return a*x + b

    def predictx(y, a, b):
        return (y-b)/a

    # Vetor da base e vetor normal a base 
    import numpy as np    
    M,N = np.nonzero(segmentation)
    minN = np.min(N)
    maxN = np.max(N) 
    minM = segmentation[:,minN].nonzero()[0].mean()
    maxM = segmentation[:,maxN].nonzero()[0].mean()
    p1 = np.array([minM, minN])
    p2 = np.array([maxM, maxN])

    base_v = p2 - p1
    base_length = np.sqrt((base_v**2).sum())
    base_v = base_v / np.sqrt((base_v**2).sum())
    cut_v = np.array([-base_v[1], base_v[0]])

    # Coeficientes das retas
    hofer = np.array([1.0/6, 1.0/2, 2.0/3, 3.0/4]).reshape(4,1)
    witelson = np.array([1.0/3, 1.0/2, 2.0/3, 4.0/5]).reshape(4,1)

    if scheme == 'HOFER':
        P = p1 + hofer*base_length*base_v

    if scheme == 'WITELSON':
        P = p1 + witelson*base_length*base_v

    p3, p4, p5, p6 = P

    rbase_A = base_v[0]/base_v[1]
    rbase_B = p1[0]-rbase_A*p1[1]
    rA = cut_v[0]/cut_v[1]
    r3B = coef_linear(rA, p3)
    r4B = coef_linear(rA, p4)
    r5B = coef_linear(rA, p5)
    r6B = coef_linear(rA, p6)

    # Rotulação da máscara    
    H,W = np.shape(segmentation)
    Parcellation = np.zeros((H,W), dtype='int')

    y,x = segmentation.nonzero()
    labels = np.zeros(y.size, dtype='int')
    above_base = y <= predicty(x, rbase_A, rbase_B)
    left_r3 = x <= predictx(y, rA, r3B)
    left_r4 = x <= predictx(y, rA, r4B)
    left_r5 = x <= predictx(y, rA, r5B)
    left_r6 = x <= predictx(y, rA, r6B)

    labels[np.logical_and(left_r3==False, left_r4)] = 2
    labels[np.logical_and(left_r4==False, left_r5)] = 3
    labels[np.logical_and(left_r5==False, left_r6)] = 4
    labels[np.logical_or(np.logical_and(above_base==False, left_r4), left_r3)] = 1
    labels[np.logical_or(np.logical_and(above_base==False, left_r5==False), left_r6==False)] = 5

    Parcellation[segmentation] = labels
    return Parcellation

