'''

Leia um número inteiro e informe se ele é positivo ou negativo, considere o 0 como positivo.

'''


print("DIGITE UM NÚMERO INTEIRO: ")
value = int(input())

if value > -1:
    print("O valor", value, "é um número positivo")
else:
    print("O valor", value, "é um número negativo")