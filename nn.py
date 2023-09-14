from tensorflow import keras
from tensorflow.keras import layers
from keras.optimizers import Adam
import numpy as np

def define_model():
    input_shape=106
    model = keras.Sequential([
        layers.Input(shape=(input_shape,)),
        layers.Dense(512,activation='linear'),
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(512,activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(512,activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.2),
        layers.Dense(2,activation='linear')
    ])

    model.compile(optimizer='adam',    
                  loss='mean_squared_error',  
                  metrics='mse')  
    return model

def params(T):
  T+=1
  x=np.arange(0, np.pi/2, np.pi/(T*2))
  a=np.cos(x)
  b=1-a
  a_=np.zeros(T)
  a_[0]=a[0]
  for i in range(T-1):
      a_[i+1]=a[i+1]*a_[i]
  b_=1-a_
  return a, b, a_, b_
  
