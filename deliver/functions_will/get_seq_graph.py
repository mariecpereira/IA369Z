# -*- encoding: utf-8 -*-
import numpy as np

def get_seq_graph(edge):

    dy, dx = np.array([-1,0,1,1,1,0,-1,-1]), np.array([-1,-1,-1,0,1,1,1,0])
    def get_neighbors(node):
        Y, X = node[0]+dy, node[1]+dx
        neighbors = edge[Y, X]
        Y, X = Y[neighbors], X[neighbors]
        return zip(Y,X)
    graph = {}
    Y, X = edge.nonzero()
    for node in zip(Y,X):
        graph[node] = get_neighbors(node)
    seq = []
    first_el = (Y[0], X[0])
    seq.append(first_el)
    ext_el = first_el
    act_el = graph[ext_el][0]
    while (first_el != ext_el) or (len(seq)==1):
        ind_el = np.where(np.array(graph[(ext_el)])!=act_el)
        ind_el_uq = np.unique(ind_el[0])

        if len(ind_el_uq)==1:
            ind_el = ind_el_uq[0]
        else:
            acum_dist = []
            for ind in ind_el_uq:
                dist_ = (graph[(ext_el)][ind][0]-ext_el[0])**2+(graph[(ext_el)][ind][1]-ext_el[1])**2
                acum_dist.append(dist_)
            min_dist = acum_dist.index(min(acum_dist))
            ind_el = ind_el_uq[min_dist]

        act_el = ext_el
        ext_el = graph[(act_el)][ind_el]
        seq.append(ext_el)
    lst1, lst2 = zip(*seq)
    return (np.array(lst1), np.array(lst2))

