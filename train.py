import tensorflow as tf
from nn import define_model, params
from feature_embedding import data_load, embedding

def train(model, a, b, a_, b_, T, ori_coords, rms):
  L=ori_coors.shape[0]
  for t in renge(T):
    e=np.random.normal(0, 1, (L,2))
    coords=np.sqrt(a_[t])*ori_coords+np.sqrt(b_[t])*e
    features=embedding(num, t, coords, rms)
    

def main():
  T=1000
  model=define_model()
  a, b, a_, b_=params(T)
  for num in range(1):
    ori_coodrs, rms=data_load(num)
    train(model, a, b, a_, b_, T, ori_coodrs, rms)

if __name__ == "__main__":
    main()
