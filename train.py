import tensorflow as tf
from nn import define_model, params
from feature_embedding import data_load, embedding

def train(model, a, b, a_, b_, T, ori_coords, rms):
  L=len(ori_coors)
  for t in renge(T):
    coords=[]
    for i in range(L):
      e=np.random.normal(0, 1, (len(ori_coords[i]),2))
      e=list(e)
      coords.append(np.sqrt(a_[t])*ori_coords[i]+np.sqrt(b_[t])*e)
    coords[:][-1]=coords[:][0]
    features=embedding(num, t, coords, rms)
    model.fit(features, e, epochs=100, batch_size=min(32,L))
  model.save("/Users/satomotoki/Desktop/model/file")
  
    

def main():
  T=1000
  model=define_model()
  a, b, a_, b_=params(T)
  for num in range(1):
    ori_coodrs, rms=data_load(num)
    train(model, a, b, a_, b_, T, ori_coodrs, rms)

if __name__ == "__main__":
    main()
