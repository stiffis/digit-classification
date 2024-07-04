import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
average_images = np.zeros((10, 8, 8))

# promedio para cada dígito
for digit in range(10):
    digit_images = digits.images[digits.target == digit]
    # Calcular el promedio de las imágenes
    average_images[digit] = np.mean(digit_images, axis=0)

# mostrar las imágenes
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(average_images[i], cmap='gray')


plt.tight_layout()
plt.show()
