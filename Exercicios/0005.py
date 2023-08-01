'''

Leia um número inteiro e apresente a seguinte menssagem:
Caso valor entre > 1 e 9 ====> O valor está na faixa permitida
Caso valor entre > menor que 1 OU maior que 9  ===> O valor está fora da faixa permitida.
'''

print("Digite o primeiro número: ")
value = int(input())

if value < 1 or value > 9:
    print("O valor está fora da faixa permitida para esta operação!")
else:
    print("O valor está dentro da faixa permitida para esta operação!")