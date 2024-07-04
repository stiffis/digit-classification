#una capa oculta con 2 "neuronas"

import numpy as np
#training data
X = np.array([[0,0],
             [0,1],
             [1,0],
             [1,1]])
#Input
Y =np.array([[0],#no olvidar el doble corchete
             [1],
             [1],
             [0]])#Output REAL
#First weight
weights1 = np.random.rand(2,2)#investigar más 
weights2 = np.random.rand(2,1)

#training parameters
    #epoch
epochs = 10000 #no olvidar mencionar en la expo las epocas ‼️
    #learning rate
learning_reate = 0.1

for epoch in range(epochs):
    for i in range(len(X)):
        x_for_input = X[i].reshape(2,1)#2,1 por que la matriz tiene q ser vertical y no horizaontal
        x_real = Y[i].reshape(1,1)#1,1 por que al inicio me devuelve una lista pero YO quiero una matriz de un solo elemento
        