# -*- encoding: utf-8 -*-
def pil_array(pil):
    import numpy
    w, h = pil.size
    binary = 0
    if pil.mode == '1':
        binary = 1
        pil = pil.convert('L')
    if pil.mode == 'L':
        d = 1 ; shape = (h,w)
    elif pil.mode == 'P':
        if 0:   # len(pil.palette.data) == 2*len(pil.palette.rawmode):
            binary = 1
            pil = pil.convert('L')
            d = 1 ; shape = (h,w)
        else:
            pil = pil.convert('RGB')
            d = 3 ; shape = (h,w,d)
    elif pil.mode in ('RGB','YCbCr'):
        d = 3 ; shape = (h,w,d)
    elif pil.mode in ('RGBA','CMYK'):
        d = 4 ; shape = (h,w,d)
    else:
        raise TypeError, "Invalid or unimplemented PIL image mode '%s'" % pil.mode
    arr = numpy.reshape(numpy.fromstring(pil.tostring(), 'B', w*h*d), shape)
    if d > 1:
        arr = numpy.swapaxes(numpy.swapaxes(arr, 0, 2), 1, 2)
    if binary:
        arr = arr.astype('?')
    return arr

