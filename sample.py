import tensorflow as tf
from feature_embedding import data_load, embedding

def sample(a, b, a_, b_):
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
            coords.append(coord)
        rm = G.nodes[i]['room_type']
        rms.append(rm)
    coords=np.array(coords)
    e=np.random.normal(0,1,(coords.shape[0], 2))
    for t in range(T):
      t=1000-t
      features=embedding(t, coords, rms, edges, n)
      pre_e=model.predict(features)
      u=np.random.normal(0,1,(coords.shape[0], 2))
      if t==1:
        coords=(coords-pre_e*b[t]/np.sqrt(b_[t]))
      else:
        coords=(coords-pre_e*b[t]/np.sqrt(b_[t]))+b[t]*u
    visialaze(coords, rms, edges, n)

def visialaze(coords, rms, edges, n):
  polys=[]
  cnt=0
  for i in range(n):
    coord=[]
    for j in range(edges[i]):
      coord.append(coords[cnt])
      cnt+=1
    poly=Polygon(coord)
    polys.append(poly)
