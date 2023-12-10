# 2. Faça a leitura de uma imagem de entrada 2D colorida qualquer e aplique o
# filtro da média, mediana e gaussiano na imagem de entrada. Mostre os
# resultados de cada filtro por meio da biblioteca matplotlib.

import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('dogs.jpg')  

if imagem is None:
    print('Erro ao carregar a imagem.')
else:
   imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

media = cv2.blur(imagem_gray, (5, 5))

mediana = cv2.medianBlur(imagem_gray, 5)

gaussiano = cv2.GaussianBlur(imagem_gray, (5, 5), 0)

plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1), plt.imshow(imagem_gray, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(media, cmap='gray')
plt.title('Filtro da Média'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(mediana, cmap='gray')
plt.title('Filtro da Mediana'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(gaussiano, cmap='gray')
plt.title('Filtro Gaussiano'), plt.xticks([]), plt.yticks([])

plt.show()
