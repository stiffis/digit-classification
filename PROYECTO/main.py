from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
# this is for the google colab notebooks
# import google.colab.files as files
#
#
#
# ------- DISTANCIA EUDLIDIANA ------


def euclidean_distance(matrix1, matrix2):
    return np.sqrt(np.sum((matrix1 - matrix2) ** 2))


def find_closest_index_digits(new_digit_matrix, digits_matrices, num_closest=3):
    distances = []
    for i, digit_matrix in enumerate(digits_matrices):
        dist = euclidean_distance(new_digit_matrix, digit_matrix)
        distances.append((i, dist))

    # Función para obtener el segundo elemento de la tupla
    def get_distance(tuple_element):
        return tuple_element[1]

    distances.sort(key=get_distance)
    closest_indices = [idx for idx, _ in distances[:num_closest]]
    return closest_indices

# ------ MOSTRAMOS EL PROMEDIO DE IMÁGENES DE X NUMERO ------


digits = load_digits()

digit = int(input("Ingrese un numero del 0 al 9: "))

digit_images = digits.images[digits.target == digit]

average_matrix = np.mean(digit_images, axis=0)
rounded_average_matrix = np.round(average_matrix)

fig, ax = plt.subplots()
c = ax.imshow(rounded_average_matrix, cmap='gray_r')
plt.title(f"Imagen promedio del número {digit}")
plt.show()

print(digit_images)
print()
# este si imprime la matriz promediada
print(f"Matrix promedio de: {digit}")
print(rounded_average_matrix)

# ------ CARGAMOS LA NUEVA IMAGEN ------

new_digit = cv2.imread('imagen_buena.png', cv2.IMREAD_GRAYSCALE)
image_new = cv2.resize(new_digit, (8, 8))

# ------ PROCESAMOS LA IMAGEN ------


def process_image(image):
    new_digit = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    image_new = cv2.resize(new_digit, (8, 8))

    image_new = 255 - image_new

    image_new = (image_new / 255.0) * 16
    image_new = np.clip(image_new, 0, 16)

    return np.round(image_new)


image_new = process_image("imagen_buena.png")
print()
print("Matriz de la imagen ingresada")
print(image_new)

# ------ MOSTRAMOS LA IMAGEN ------

fig, ax = plt.subplots()
c = ax.imshow(image_new, cmap='gray_r')
plt.title("Imagen procesada")
plt.show()

# ------ INDICES MAS CERCANOS -> DIGITOS MAS CERCANOS ------

# Es esta línea vamos a encontrar los índices más cercanos
closest_i = find_closest_index_digits(
    image_new, digits.images)  # solo clset digits

# Ya que encontramos los índices con respecto a esto encontraremos los dígitos
closest_d = [int(digits.target[x]) for x in closest_i]

# A partir de esto verificamos si hay coincidencias en los dígitos más cercanos
target_c = {}  # contador de targets
for digit in closest_d:
    if digit in target_c:
        target_c[digit] += 1
    else:
        target_c[digit] = 1

print(f"3 Dígitos más cercanos: {closest_d}")


max_count = max(target_c.values())
if max_count >= 2:
    detec_digit = [k for k, v in target_c.items() if v == max_count][0]
    print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {
          detec_digit}")
else:
    for num_closest in range(4, len(digits.images)):

        distances = []
        for i, digit_matrix in enumerate(digits.images):
            dist = euclidean_distance(image_new, digit_matrix)
            distances.append((i, dist))

        # En esta parte vamos a convertir a Dataframe con .head
        distances_df = pd.DataFrame(distances, columns=['ix', 'dist'])

        sorted_dist_df = distances_df.sort_values(by='dist')
        closest_indices = sorted_dist_df.head(num_closest)['ix']

        closest_d = [int(digits.target[k]) for k in closest_indices]
        target_counts = {}
        for d in closest_d:
            if d in target_counts:
                target_counts[d] += 1
            else:
                target_counts[d] = 1

        max_count = max(target_counts.values())
        if max_count >= 2:
            detec_digit = [k for k, v in target_counts.items()
                           if v == max_count][0]
            print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {
                  detec_digit}")
            break
# guardando csv
distances = []
for i, digit_matrix in enumerate(digits.images):
    dist = euclidean_distance(image_new, digit_matrix)
    distances.append((i, dist))

distances_df = pd.DataFrame(distances, columns=['ix', 'dist'])
sorted_dist_df = distances_df.sort_values(by='dist')

# Guardamos el DataFrame como CSV y lo descargamos
sorted_dist_df.to_csv("data.csv", index=False)
# this is for download the file from google colab
# files.download('data.csv')


average_matrices = []
for i in range(10):
    digit_images = digits.images[digits.target == i]
    average_matrix = np.mean(digit_images, axis=0)
    rounded_average_matrix = np.round(average_matrix)
    average_matrices.append(rounded_average_matrix)

distances = [euclidean_distance(image_new, avg_matrix)
             for avg_matrix in average_matrices]

min_distance = min(distances)
detec_digit = distances.index(min_distance)

print(f"\nSoy la inteligencia artificial version 2, y he detectado que el digito ingresado corresponde al numero {
      detec_digit}")
