"""
LEIA OS 5 VALORES INSERIDOS PELO USUÁRIO E EM SEGUIDA MOSTRe A QUANTIDADE DE
NÚMEROS NEGATIVOS QUE FORAM INSERIDOS PELO MESMO.

"""

negativos = 0
numero = 0

for i in range(1, 6):
    print("Digite um número: ")
    numero = float(input())
    if numero < 0:
        negativos += 1

print(f"A quantidade de números negativos inseridos foram: {negativos}")

