#-- COLEÇÕES - CURSO Python Básico - IA EXPERT ACADEMY
    # Tuplas, Listas, Dicionários, conjuntos (SET)

#-- DICIONÁRIOS

coletaMosquitos = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
#--     'CHAVES': VALORES

print(' foram coletados', coletaMosquitos['Aedes aegypt'], ' mosquitos da espécie Aedes aegypt')
print(' foram coletados', coletaMosquitos['Aedes albopictus'], ' mosquitos da espécie Aedes albopictus')
print(' foram coletados', coletaMosquitos['Anopheles darlingi'], ' mosquitos da espécie Anopheles darlingi')

#-- Adicionando elemento ao dicionário

coletaMosquitos['Rhodnius montenegrensis'] = 11

print(f'\nDicionário Atualizado: {coletaMosquitos}')

#-- Excluindo valor com função del()

#-- del(coletaMosquitos) <- Neste caso excluirá _todo o dicionário

#-- EXCLUINDO UM ITEM DO DICIONÁRIO

del(coletaMosquitos['Aedes aegypt'])

print(f'\nDicionário com a exclusão do item \'Aedes aegypt\': {coletaMosquitos}')

#-- Chamando a função de itens completos do dicionário com suas respectivas chaves e valores
print('\n')
print(100 * '*')
# CHAVES E VALORES - COMPLETOS
print(coletaMosquitos.items(), '\n')
# CHAVES
print(coletaMosquitos.keys(), '\n')
#VALORES
print(coletaMosquitos.values(), '\n')
print(100 * '*')

#--
# Criando um novo dicionário

coletaMosquitosZonaDois = {'Anopheles gambiae': 13, 'Anopheles dearneorim': 14}

#--

print('\n')
print(f'Esse é o novo dicionário criado: {coletaMosquitosZonaDois}')

#--

#--
# Fazendo o Update do dicionário 01, o comando .update vai concatenar o dicionário 01 ao dicionário 02.

coletaMosquitos.update(coletaMosquitosZonaDois)

print(f'\nEsse é o Dicionário 01 atualizado: {coletaMosquitos}')

print('\n', coletaMosquitos.items())
print('\n')

for especie, numeroEspecimes in coletaMosquitos.items():
    print(f'Nome: {especie}. Quantidade coletada: {numeroEspecimes}')
#--


#-- CONJUNTOS --

# Tupla com dados repetidos para serem analisados pelo set() e formar um conjunto sem repetições;
print('\n')
biomoleculas = ('Proteína', 'ácidos nucleicos', 'carboidratos', 'lipídeo',
                'ácidos nucleicos', 'carboidratos', 'carboidratos', 'carboidratos')

print(biomoleculas)

print('\n')

#-- USANDO O SET PARA RETIRAR OS ITENS REPETIDOS E FORMA O CONJUNTO DE ELEMENTOS ÚNICOS;

print(set(biomoleculas))

print('\n')

#-- CRIAREMOS DOIS CONJUNTOS NOVOS

conjunto_01 = {1, 2, 3, 4, 5}
conjunto_02 = {3, 4, 5, 6, 7}

#-- USAREMOS A INTERSECÇÃO DE CONJUNTOS PARA OS ELEMENTOS CRIADOS
intersectionConj_01Conj_02 = conjunto_01.intersection(conjunto_02)
print(f'\nEsse é o conjunto {conjunto_01}')
print(f'Esse é o conjunto {conjunto_02}')
print('\n')
print('ESSA É A INTERSECÇÃO DOS CONJUNTOS 01 COM 02!')
print(intersectionConj_01Conj_02)
print('\n')

#--
# DIFERENÇA ENTRE OS CONJUNTOS

print(conjunto_01.difference(conjunto_02))
print(conjunto_02.difference(conjunto_01))



















