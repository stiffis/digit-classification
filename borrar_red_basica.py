import numpy as np
#training data
X = np.array([1, 2, 3, 4, 5])#Input
Y = 0.5*X#Output REAL
#First weight
W = np.random.rand()#vacio por que solo te da un entero aleatorio
#training parameters
    #epoch
epochs = 1000 #no olvidar mencionar en la expo las epocas ‼️
    #learning rate
learning_reate = 0.01

for epoch in range(epochs):
    for x, y_real in zip(X, Y):
        y_pred=x*W
        error = y_pred -y_real

        #gradient
        gradient=error*x

        #Updating w
        W=W-gradient*learning_reate #W-=gradient*learning_rate
    if epoch%100==0:
        print(W)

