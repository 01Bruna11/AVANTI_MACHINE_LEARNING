import pandas as pd

# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

print("Exercício 1: \n")

def eh_primo(numero):
    numero = int(numero)
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_na_lista(lista):
    primos = [int(numero) for numero in lista if eh_primo(numero)]
    return primos

lista_de_numeros = input("Digite uma lista de números separados por espaço: ").split()
primos_encontrados = numeros_primos_na_lista(lista_de_numeros)
print(primos_encontrados)

print("\n")
print("--------------------------------------------------------------")
# 2. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

print("Exercício 2: \n")

def elementos_em_apenas_uma_lista(lista1, lista2):
    exclusivos = list(set(lista1) ^ set(lista2))
    return exclusivos

lista1 = input("Digite uma lista de números separados por espaço: ").split()
lista2 = input("Digite outra lista de números separados por espaço: ").split()
resultado = elementos_em_apenas_uma_lista(lista1, lista2)
print(resultado)

print("\n")
print("--------------------------------------------------------------")

# 3. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

print("Exercício 3: \n")

def segundo_maior(lista):
    if len(lista) < 2:
        return None  
    
    lista = [int(numero) for numero in lista]
    
    maior = segundo = float('-inf')
    
    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo and numero != maior:
            segundo = numero
    
    if segundo == float('-inf'):
        return None
    
    return segundo

lista_de_numeros = input("Digite uma lista de números separados por espaço: ").split()
segundo_maior_valor = segundo_maior(lista_de_numeros)

if segundo_maior_valor is not None:
    print(f"O segundo maior valor na lista é: {segundo_maior_valor}")
else:
    print("A lista não tem um segundo maior valor.")

print("\n")
print("--------------------------------------------------------------")
# 4. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

print("Exercício 4: \n")

def ordenar_por_nome(lista_de_pessoas):
    lista_ordenada = sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])
    return lista_ordenada

lista_de_pessoas = input("Digite uma lista de pessoas e suas idades separados por espaço: ").split()
lista_ordenada = ordenar_por_nome(lista_de_pessoas)

print("Lista original:", lista_de_pessoas)
print("Lista ordenada pelo nome:", lista_ordenada)

print("\n")
print("--------------------------------------------------------------")

# 5. Dada uma lista contendo números inteiros, como você encontraria o maior número e o menor número dessa lista em uma única passagem?

print("Exercício 5: \n")
def encontrar_maior_menor(lista):
    if not lista:
        return None, None  

    maior = menor = lista[0]

    for numero in lista[1:]:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor

lista_de_numeros = input("Digite uma lista de números separados por espaço: ").split()
maior, menor = encontrar_maior_menor(lista_de_numeros)

print(f"O maior número na lista é: {maior}")
print(f"O menor número na lista é: {menor}")

print("\n")
print("--------------------------------------------------------------")
# 6. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

print("Exercício 6: \n")

nome_arquivo = 'teste.csv'

try:
    dataframe = pd.read_csv(nome_arquivo, encoding='ISO-8859-1')
    print(dataframe.head())
except UnicodeDecodeError:
    print("Erro de decodificação. Tente especificar outro encoding.")

print("\n")
print("--------------------------------------------------------------")
# 7. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

print("Exercício 7: \n")
dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
         'Idade': [25, 30, 35, 40],
         'Cidade': ['A', 'B', 'A', 'C']}

df = pd.DataFrame(dados)

linhas_filtradas = df[df['Idade'] > 30]

print(linhas_filtradas)
print("\n")
print("--------------------------------------------------------------")
# 8. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

print("Exercício 8: \n")
dados = {'A': [1, 2, None, 4, 5],
         'B': [10, None, 30, 40, 50],
         'C': [100, 200, 300, 400, None]}

df = pd.DataFrame(dados)

print(df.isnull())

# 9. complete o código

print("Exercício 9: \n")

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), constrained_layout=True)

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               xycoords="axes fraction",
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')

fig.suptitle('plt.subplots()')
plt.show()

print("\n")
print("--------------------------------------------------------------")

# 10. complete o código

print("Exercício 10: \n")
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

print("\n")


