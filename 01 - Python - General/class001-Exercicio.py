#-- Exercício 001 - CURSO Python Básico - IA EXPERT ACADEMY
    # Tuplas, Listas, Dicionários, conjuntos (SET)

    # A) Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
    # e os armazeneos dentro de uma lista. Após a leitura, crie outra estrutura de repetição
    # para somar os valores armazenados.

import numpy as np


lista = []

for i in range(1, 6):
    value = int(input("Digite um valor: "))
    lista.append(value)
#--

print(lista)

soma = 0
for i in range(len(lista)):
    soma += lista[i]
#--

print(soma)

#--

print(f'\nSOMA COM NUMPY: {np.array(lista).sum()}')

#--

    # B) Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores,
    # através de uma estrutura de repetição. Depois crie uma nova estrutura de repetição para somar
    # todas as notas e retornar a média final.


alunos = {}

for i in range(1, 4):
    nome = input("Digite o nome do Aluno: ")
    nota = float(input("Digite a nota do Aluno: "))
    alunos[nome] = nota
#--

#--

soma = 0
for nota in alunos.values():
    soma += nota
#--

media = soma / 3


print(f'As notas dos alunos seguem: {alunos}')
print(f'A média aritimética entre as notas é de: {media}')


#--

    # C) Dada a matriz abaixo:
        # Construa uma estrutura de repetição para percorrer e somar todos
        # os elementos da matriz;

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

print(matriz.shape)
print(matriz)

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
     soma += matriz[i][j]
#--

print(f'A soma da matriz é igual: {soma}')









