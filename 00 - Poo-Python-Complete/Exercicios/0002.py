'''
Leia dois números inteiros e informe qual deles é o maior. Se os números forem iguais, mostre ao usuário
esta informação.

'''

print("Digite o primeiro número: ")
value01 = int(input())

print("Digite o segundo número: ")
value02 = int(input())

if value01 > value02:
    print(f"O Número {value01} é maior que o número {value02}")
elif value02 > value01:
    print(f"O Número {value02} é maior que o número {value01}")
else:
    print(f"O numero {value01} é igual ao número: {value02}")
