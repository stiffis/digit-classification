#una capa oculta con 2 "neuronas"

import numpy as np
#training data
X = np.array([[0,0],
             [0,1],
             [1,0],
             [1,1]])
#Input
Y =np.array([0,
             1,
             1,
             0])#Output REAL
#First weight
W = np.random.rand()#vacio por que solo te da un entero aleatorio
#training parameters
    #epoch
epochs = 1000 #no olvidar mencionar en la expo las epocas ‼️
    #learning rate
learning_reate = 0.01