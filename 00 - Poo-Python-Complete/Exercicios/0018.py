'''
Ler dados e informar se o mesmo é + ou -
função para ler dados
Função para apresentar resultado
'''

numero = 0


def entradaDados(msn):
    global numero
    print(msn)
    numero = float(input())
# end

def result(num):

    if num >= 0:
        print(f"O número {num}: é positivo. ")
    else:
        print(f"O número é {num}: é negativo. ")
# end


if __name__ == '__main__':
    entradaDados("Digite um número: ")
    result(numero)

