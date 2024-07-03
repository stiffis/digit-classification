import cv2

mi_imagen = cv2.imread("imagen_buena.pnge", cv2.IMREAD_GRAYSCALE)
imagen_pequena = cv2.resize(mi_imagen,(8,8))

#invertimos los colores

i = 0
while i <= 7:
    j = 0
    while j <= 7:
        imagen_pequena[i][j] = 255 - imagen_pequena[i][j]
        j += 1
    i += 1
for x in range(8):
    for y in range():
        imagen_pequena[x][y] = 255 - imagen_pequena[x][y]

# aplicamos el martillo bonk ( 255 baja a 16 )

i = 0
while i <= 7: # esto se puede reemplazar con for
    j = 0
    while j <= 7:
        imagen_pequena[i][j] = imagen_pequena[i][j] / 255 * 16
        j += 1
    i += 1
print(imagen_pequena)
