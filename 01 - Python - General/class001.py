#-- COLEÇÕES - CURSO Python Básico - IA EXPERT ACADEMY
    # Tuplas, Listas, Dicionários, conjuntos (SET)

#-- TUPLAS

tupla = ('Homo sapiens', 'Canis familiaris', 'Filis catus')

print(tupla[0])
print(tupla[1])
print(tupla[2])

print(tupla.index('Canis familiaris')) # Consulta o Index do conteúdo na Tupla
print(tupla.index('Filis catus')) # Consulta o Index do conteúdo na Tupla
print(tupla.index('Homo sapiens')) # Consulta o Index do conteúdo na Tupla

# Vai buscar o conteúdo na variável tupla e em seguida transferirar todos para o Elemento!
for elemento in tupla:
    print(elemento)
#--


#-- LISTAS
print('\n')

lista_01 = ['Homo sapiens', 'Canis familiaris', 'Filis catus']
lista_02 = ['Xenopolis laevis', 'Ailuropoda melanoleuca']

l1_U_l2 = lista_01 + lista_02

print(f'Essa é a lista 01: {lista_01}')
print(f'Essa é a lista 02: {lista_02}')
print(f'Essa é a União da lista 01 com a 02: {l1_U_l2} \n')

lista_03 = lista_02 * 2 #--
lista_04 = lista_02 * 3 # A Variável ira armazena os valores da lista 2 multiplicando e triplicando

print(f'Lista 02 Duplicada: {lista_03}')
print(f'Lista 02 Triplicada: {lista_04} \n')

print(lista_01[0:2], '\n') # Vai buscar na lista 01 a posição 0 até 02;
print(lista_02[1], '\n') # Vai buscar na lista 02 a posição 1;

lista_01.append('Gorila gorila') # O Append vai adicionar um novo item a lista
print(f'Essa é a lista 01 - Item Adicionado{lista_01}')

lista_01.remove('Canis familiaris') # O Remove vai remover o item escolhida da lista

print(f'Essa é a lista 01 - Item Removido {lista_01}\n')

# Vai buscar o conteúdo na lista 01 e em seguida transferirar todos para a variável itemLista!
for itemLista in lista_01:
    print(itemLista)
#--
print('\n')

print(f'Lista 04 antes da exclusão: {lista_04}')

del(lista_04) # A Função del(), vai excluir a lista inteira!

print('AGORA VAI GERAR UM ERRO - POIS FOI USADA A FUNÇÃO DEL() PARA EXCLUIR A LISTA INTEIRA!\n')

print(lista_04)











