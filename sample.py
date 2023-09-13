import numpy as np
from PIL import Image
import tensorflow as tf
import pickle
from shapely.geometry import Polygon
from shapely.geometry import Point
from feature_embedding import data_load, embedding
from nn import params

def sample(a, b, a_, b_, T):
  model=tf.keras.models.load_model("/Users/satomotoki/Desktop/model/file")
  for num in range(1):
    with open('/Users/satomotoki/Desktop/modified-swiss-dwellings-v1-train_50/graph_out_50/'+str(num)+'.pickle', 'rb') as file:
        G = pickle.load(file)
    n = G.number_of_nodes()
    coords = []
    rms = []
    edges=[]
    for i in range(n):
        poly = Polygon(G.nodes[i]['geometry'])
        coord = list(poly.exterior.coords)
        edges.append(len(coord)-1)
        for j in range(len(coord)-1):
            coords.append(coord[j])
        rm = G.nodes[i]['room_type']
        rms.append(rm)
    coords=np.array(coords)
    e=np.random.normal(0,1,(coords.shape[0], 2))
    for t in range(T):
      t=T-t
      features=embedding(t, coords, rms, edges, n)
      pre_e=model.predict(features)
      u=np.random.normal(0,1,(coords.shape[0], 2))
      if t==1:
        coords=(coords-pre_e*b[t]/np.sqrt(b_[t]))
      else:
        coords=(coords-pre_e*b[t]/np.sqrt(b_[t]))+b[t]*u
    visialaze(coords, rms, edges, n)

def visialaze(coords, rms, edges, n):
  color=np.zeros((14,3))
  color[0]=[255,0,255]#fuchsia
  color[1]=[128,128,128]#gray
  color[2]=[0,255,0]#lime
  color[3]=[0,0,255]#blue
  color[4]=[128,0,0]#maroon
  color[5]=[128,128,0]#olive
  color[6]=[192,192,192]#silver
  color[7]=[255,0,0]#red
  color[8]=[0,128,0]#green
  color[9]=[0,0,128]#navy
  color[10]=[255,255,0]#yellow
  color[11]=[0,255,255]#aqua
  color[12]=[128,0,128]#purple
  color[13]=[255,255,255]#white
  data=no.zeros((256,256,3))

  min_x=100000
  max_x=-100000
  min_y=100000
  max_y=-100000
  for c in coords:
    min_x=min(c[0], min_x)
    max_x=max(c[0], max_x)
    min_y=min(c[1], min_y)
    max_y=max(c[1], max_y)
  X=max_x-min_x
  Y=max_y-min_y
  r=0.125
  min_x-=r*X
  max_x+=r*X
  min_y-=r*Y
  max_y+=r*Y
  X=max_x-min_x
  Y=max_y-min_y
  D=max(X,Y)
  dx=(D-X)/2
  dy=(D-Y)/2
  fixed_coords=[]
  for c in coords:
    x=int(255*(c[0]+dx-min_x)/D)
    y=int(255*(c[1]+dy-min_y)/D)
    fixed_coords.append((x,y))
  
  polys=[]
  cnt=0
  for i in range(n):
    coord=[]
    for j in range(edges[i]):
      coord.append(fixed_coords[cnt])
      cnt+=1
    poly=Polygon(coord)
    polys.append(poly)
  data[:,:,:]=color[13]
  for i in range(256):
    for j in range(256):
      point = Point(i, j)
      for k in range(14):
        if polys[k].contains(point):
          data[i,j,:]=color[rms[k]]
  image_data = (data).astype(np.uint8)
  image = Image.fromarray(image_data)
  image.save('/Users/satomotoki/Desktop/output/file')

def main():
  T=100
  a, b, a_, b_=params(T)
  for num in range(1):
    sample(a, b, a_, b_, T)

if __name__ == "__main__":
    main()
