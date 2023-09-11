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
    e=
    for t in range(T):
      t=1000-t
      features=embedding(t, coords, rms)
      pre_e=model.predict(features)
      e_coords=[]
      u_coords=[]
      cnt=0
      for i in range(n):
        e=[]
        u=p.random.normal(0, 1, (len(coords[i]),2))
        u[-1]=u[0]
        for j in range(len(coords[i])-1):
          e.append(list(pre_e[cnt]))
          cnt+=1
        e.append(e[0])
        e_coords.append(e)
        u_coords.append(u)
      if t==1:
        coords=(coords-e_coords*b[t]/np.sqrt(b_[t]))
      else:
        coords=(coords-e_coords*b[t]/np.sqrt(b_[t]))+b[t]*u_coords
    vi
