from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos de dígitos
digits = load_digits()

# Calcular y mostrar los promedios para cada dígito del 0 al 9
for digit in range(10):
    # Filtrar las matrices del número específico
    digit_images = digits.images[digits.target == digit]
    
    # Calcular el promedio de las imágenes
    average_matrix = np.mean(digit_images, axis=0)
    
    # Redondear la matriz promedio al entero más cercano
    rounded_average_matrix = np.round(average_matrix)
    
    # Mostrar la matriz promedio usando matplotlib
    print(f"Promedio para el número {digit}:")
    print(rounded_average_matrix)
    print(f"Cantidad de muestras para el número {digit}: {len(digit_images)}\n")
    
    # Mostrar la imagen usando matplotlib
    fig, ax = plt.subplots()
    c = ax.imshow(rounded_average_matrix, cmap='gray_r')
    plt.title(f"Promedio para el número {digit}")
    plt.colorbar(c)
    plt.show()
