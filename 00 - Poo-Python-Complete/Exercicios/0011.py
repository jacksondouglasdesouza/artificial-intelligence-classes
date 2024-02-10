#FOR in Python

'''
for i in range(6, -1, -1):
    print(f"Valor de {i}")
'''


nota = 0
soma = 0
for i in range(1, 6):
    print("Digite a primeira nota: ")
    nota = float(input())
    soma += nota
    print(f"O Acumulado de notas é: {soma}")

media = soma / 5

print(f"A média aritimética é: {media}")

