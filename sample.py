def sample(a, b, a_, b_):
  for num in range(1):
    with open('/Users/satomotoki/Desktop/modified-swiss-dwellings-v1-train_50/graph_out_50/'+str(num)+'.pickle', 'rb') as file:
        G = pickle.load(file)
    n = G.number_of_nodes()
    coords=[]
    rms=[]
    for i in range(n):
      poly = Polygon(G.nodes[i]['geometry'])
      coord = list(poly.exterior.coords)
      l=len(coord)
      e=np.random.normal(0, 1, (l,2))
      e[-1]=e[0]
      coords.append(list(e))
      rm = G.nodes[i]['room_type']
      rms.append(rm)
    for t in range(T):
      t=1000-t
      if t==1
    
