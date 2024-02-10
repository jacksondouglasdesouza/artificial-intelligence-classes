#-- Matrizes - CURSO Python Básico - IA EXPERT ACADEMY

import numpy as np

#-- NP.variavel <-- o NP é a abreviação para numpy;

matriz = np.array([[1,2,3],
                   [4,5,6]])
#--

print(matriz)

#-- O .SHAPE APRESENTA O FORMATO, QUANTIDADE DE LINHAS E COLUNAS;

print(matriz.shape)

print('\n')

#-- RETORNO DAS LINHAS
print(matriz[0], 'Linha 01')
print(matriz[1], 'Linha 02')

#-- RETORNA COLUNA COM VALOR

print('Valor: ', matriz[0][0], '>>> Linha 0 e coluna 0')
print('Valor: ', matriz[0][1], '>>> Linha 0 e coluna 1')
print('Valor: ', matriz[0][2], '>>> Linha 0 e coluna 2')
#--
print('\n')
print('Valor: ', matriz[1][0], '>>> Linha 1 e coluna 0')
print('Valor: ', matriz[1][1], '>>> Linha 1 e coluna 1')
print('Valor: ', matriz[1][2], '>>> Linha 1 e coluna 2')

#-- PERCORRENTO O TOTAL DOS ELEMENTOS;

print('\n')

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
    #--
#--

print('\n')


