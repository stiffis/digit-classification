from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos de dígitos
digits = load_digits()


digit = int(input("Ingrese un numero del 0 al 9: "))

# digits.images es un 3D NumpyArray donde cada elemento 
# es de 2D representando a la imagen

# digits.target ve todos los targets (numero correspondiente) de cada array
# aqui se filtran las matrices del numero ingresado
digit_images = digits.images[digits.target == digit]

# np.mean sirve para hallar el promedio de las imagenes
# al ser un array 3D (numero de imagenes, altura, ancho)
# axis significa que trabaja con el numero de imagenes
average_matrix = np.mean(digit_images, axis = 0)
#al imprimir, me salian muchos numeros, se redondeo, al entero más cercano
rounded_average_matrix = np.round(average_matrix)

#este print no es necesario, solo esta para mejor compresion del resultado
print(digit_images)
print()
#este si imprime la matriz promediada
print(rounded_average_matrix)

#este print tampoco es necesario
print(f"La cantidad de muestras para el num {digit} son {len(digit_images)}")

## BASICAMENTE LA PARTE B

#####################################

# aqui se muestra la imagen con matplotlib
fig, ax = plt.subplots()
c = ax.imshow(rounded_average_matrix, cmap='gray_r')
plt.title(f"Promedio para el número {digit}")
plt.colorbar(c)
plt.show()