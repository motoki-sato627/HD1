from tensorflow import keras
from tensorflow.keras import layers
from keras.optimizers import Adam
import numpy as np

def define_model():
    input_shape=106
    model = keras.Sequential([
        layers.Input(shape=(input_shape,)),
        layers.Dense(512,activation='liner'),
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
  x=np.arange(0.01, np.pi/2-0.01, (np.pi/2-0.02)/T)
  b=np.sin(x)
  a=1-b
  a_=np.zeros(T)
  for i in tange(T):
    if i==0:
      a_[i]=a[i]
    else:
      a_[i]=a_[i-1]*a[i]
  b_=1-a_
  return a, b, a_, b_
  
