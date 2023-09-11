import numpy as np
import pickle
from shapely.geometry import Polygon
import data_preprocess

def data_load(num):
    with open('/Users/satomotoki/Desktop/modified-swiss-dwellings-v1-train_50/graph_out_50/'+str(num)+'.pickle', 'rb') as file:
        G = pickle.load(file)
    G = data_preprocess.preprocess(G)
    n = G.number_of_nodes()
    coords = []
    rms = []
    for i in range(n):
        poly = Polygon(G.nodes[i]['geometry'])
        coord = list(poly.exterior.coords)
        coords.append(coord)
        rm = G.nodes[i]['room_type']
        rms.append(rm)
    return coords, rms

def embedding(num, t, coords, rms):
    C = []
    for i in range(coords.shape[0]):
        for j in range(coords.shape[1]-1):
            c=[]
            for k in range(8):
                c_ = (k*coords[i][j] + (7-k)*coords[i][j+1])/7
                c.append(c_)
            c=np.array(c)
            R=np.zeros(25)
            R[rms[i]]=1
            c=np.hstack(c, R)
            i1=np.zeros(32)
            i1[i]=1
            c=np.hstack(c, i1)
            j1=np.zeros(32)
            j1[j]=1
            c=np.hstack(c, j1)
            c=np.hstack(c, t)
            C.append(c)
    C=np.array(C)
    return C
