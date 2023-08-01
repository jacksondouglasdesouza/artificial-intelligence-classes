'''
Crie um código quer receba 5 valores, sendo estes positivos ou negativos.
Após a entrada dos 5 valores o programa deve informar a quantidade de númerois negativos que foram inseridos
pelo usuário no prompt.
'''

i = 1
negativos = 0

while i <= 5:
    print("insira um número: ")
    numeros = int(input())

    if numeros < 0 and numeros != 0:
        negativos += 1

    i += 1

print(f"Total de números negativos: {negativos}")
