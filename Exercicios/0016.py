'''

def mensagem(msg, nVezes):
    for cont in range(0, nVezes):
        print(f"{msg} {cont+1}")

#-

mensagem("Nova mensagem!", 10)
'''


value01 = 0
value02 = 0
soma = 0

def entradaDados():
    print("Digite o primeiro valor: ")
    global value01
    value01 = float(input())
    print("Digite o segundo valor: ")
    global value02
    value02 = float(input())
# end


def somatorio(value1, value2):
    global soma
    soma += (value1 + value2)
# end


def result(sm):
    print(f"A soma é: {sm}")
# end


if __name__ == '__main__':
    entradaDados()
    somatorio(value01, value02)
    result(soma)

#
