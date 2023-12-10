# 1. Faça a leitura de uma imagem 2D colorida qualquer e apresente as
# informações listadas abaixo por meio da função print().
# altura, largura, Canais de cor, tipo de dado, tom de cinza máximo, tom de
# cinza médio, tom de cinza mínimo.

import cv2

imagem = cv2.imread('dogs.jpg')

if imagem is None:
    print('Erro ao carregar a imagem.')
else:
    altura, largura, canais = imagem.shape
    tipo_de_dado = imagem.dtype
    tom_de_cinza_maximo = imagem.max()
    tom_de_cinza_medio = imagem.mean()
    tom_de_cinza_minimo = imagem.min()

    print(f'Altura: {altura}')
    print(f'Largura: {largura}')
    print(f'Canais de cor: {canais}')
    print(f'Tipo de dado: {tipo_de_dado}')
    print(f'Tom de cinza máximo: {tom_de_cinza_maximo}')
    print(f'Tom de cinza médio: {tom_de_cinza_medio}')
    print(f'Tom de cinza mínimo: {tom_de_cinza_minimo}')
