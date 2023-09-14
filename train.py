import tensorflow as tf
import numpy as np
from nn import define_model, params
from feature_embedding import data_load, embedding

def train(model, a, b, a_, b_, T, ori_coords, rms, edges, n):
  for t in range(1, T+1):
    e=np.random.normal(0,1,(ori_coords.shape[0], 2))
    coords=np.sqrt(a_[t])*ori_coords+np.sqrt(b_[t])*e
    features=embedding(t, coords, rms, edges, n)
    model.fit(x=features, y=e, epochs=100, batch_size=32, verbose=0)
    if t%100==0:
      print(t)
  model.save("/Users/satomotoki/Desktop/model/file")
  
    

def main():
  T=1000
  model=define_model()
  a, b, a_, b_=params(T)
  for num in range(1):
    ori_coodrs, rms, edges, n=data_load(num)
    train(model, a, b, a_, b_, T, ori_coodrs, rms, edges, n)

if __name__ == "__main__":
    main()
