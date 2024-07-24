import cv2
import matplotlib.pyplot as plt

new_digit = cv2.imread('imagen_buena.png', cv2.IMREAD_GRAYSCALE)
image_new = cv2.resize(new_digit, (8, 8))

# Invertimos los colores de la imagen y ajustar los valores
for i in range(8):
   for j in range(8):
       image_new[i][j] = 255 - image_new[i][j]
       if image_new[i][j] == 255:
           image_new[i][j] = 0
       elif image_new[i][j] == 0:
           image_new[i][j] = 16

print(image_new)

fig, ax = plt.subplots()
c = ax.imshow(image_new, cmap='gray_r')
plt.show()

