'''

fastName = "Jackson Douglas"
lastName = "de Souza"

print(f"{fastName} {lastName}")

'''

'''
i = 1
while i <= 10:
    print(f"2 x {i} = {i * 2}")
    i += 1
'''


'''
i = 1
nota = 0
soma = 0
media = 0

while i <= 5:
    print(f"Digite a nota Nº: {i}")
    nota = float(input())
    soma = soma + nota
    media += 1
    i += 1

media = soma / media
print(soma)
print(f"A média é: {media}")
'''


#VALIDADOR

'''
nota = -1

while nota > 10 or nota < 0:
    print("Digite a nota novamente: ")
    nota = float(input())

'''

nota = 0
sim = 's'

while sim == 's':
    print("Adicione um novo valor: ")
    nota += float(input())
    print("Deseja continuar? [ s/n ]")
    sim = input()

print(f"Total: {nota}")
