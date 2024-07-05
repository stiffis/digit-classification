from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos de dígitos
digits = load_digits()

novo = []
digit = int(input("Ingrese un numero del 0 al 9: "))

# Filtrar las imágenes donde digits.target es igual a digit
digit_images = digits.images[digits.target == digit]
for x in digit_images:
    novo.append(x)

matrices_array = np.array(novo)
average_matrix = np.mean(digit_images, axis=0)
rounded_average_matrix = np.round(average_matrix)
print(digit_images)
print()
print(rounded_average_matrix)

print(print(f"La cantidad de muestras para el num {digit} son {len(digit_images)}"))

fig, ax = plt.subplots()
c = ax.imshow(rounded_average_matrix, cmap='gray_r')
plt.show()

"""
# mostrar con plt (matplotlib)
plt.figure(figsize=(8, 6))

# Mostrar la figura
plt.show()
"""