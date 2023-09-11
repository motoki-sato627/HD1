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
    edges=[]
    for i in range(n):
        poly = Polygon(G.nodes[i]['geometry'])
        coord = list(poly.exterior.coords)
        edges.append(len(coord)-1)
        for j in range(len(coord)-1):
            coords.append(coord)
        rm = G.nodes[i]['room_type']
        rms.append(rm)
    coords=np.array(coords)
    return coords, rms, edges, n

def embedding(t, coords, rms, edges, n):
    C = []
    cnt=0
    for i in range(n):
        for j in range(edges[i]):
            c=[]
            if j!=edges[i]-1
                for k in range(8):
                    c_ = (k*coords[cnt] + (7-k)*coords[cnt+1])/7
                    c.append(c_)
            else:
                for k in range(8):
                    c_ = (k*coords[cnt] + (7-k)*coords[cnt-j])/7
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
            cnt+=1
    C=np.array(C)
    return C
