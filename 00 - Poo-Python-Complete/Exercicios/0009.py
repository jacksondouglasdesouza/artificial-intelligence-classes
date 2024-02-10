'''
Leia duas notas e informe a média aritimética.
Caso o valor digitado for menor que 0, ou maior que 10, o usuário deve digitar a média novamente.
'''


i = 1
nota = 0
soma = 0

while i <= 2:

    print("Digite uma nota: ")
    nota = float(input())

    if nota < 0 or nota > 10:
        print('Nota inválida:')
        i -= 1
    else:
        soma += nota

    i += 1

media = soma / 2
print(f"A média é: {media}")
