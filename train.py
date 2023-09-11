import tensorflow as tf
from nn import define_model, params

def main():
  T=1000
  model=define_model()
  a, b, a_, b_=params(T)
  train(model, a, b, a_, b_, T)
