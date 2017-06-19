# -*- encoding: utf-8 -*-
def find_file(filename):
    '''Search image filename in sys.imagepath or sys.path.'''
    import sys, os.path
    if not os.path.isfile(filename) and not os.path.isabs(filename):
        try:
            for a in sys.imagepath:
                if os.path.isfile(os.path.join(a, filename)):
                    filename = os.path.join(a, filename)
                    break
        except:
            for a in sys.path:
                if os.path.isfile(os.path.join(a, filename)):
                    filename = os.path.join(a, filename)
                    break
    return filename

