'''
Calcule a média aritmética dos alunos e mostre se os alunos foram aprovados ou não,
considerando que para ser aprovado a média deve ser maior ou igual a 6.0

APROVADO = MEDIA >= 6
REPROVADO = MEDIA < 6

'''

print("Insira sua primeira nota: ")
value01 = float(input())
print("Insira sua segunda nota: ")
value02 = float(input())
print("Insira sua terceira nota: ")
value03 = float(input())

totalValue = value01 + value02 + value03
media = totalValue / 3

if media >= 6:
    print("*************************")
    print("A média foi: ", media)
    print("O aluno está [ APROVADO ]")
    print("*************************")

elif media < 6 and media >= 4:
    print("*************************")
    print("A média foi: ", media)
    print("O aluno está em [ RECUPERAÇÃO ]")
    print("*************************")
else:
    print("*************************")
    print("A média foi: ", media)
    print("O aluno está [ REPROVADO ]")
    print("*************************")


