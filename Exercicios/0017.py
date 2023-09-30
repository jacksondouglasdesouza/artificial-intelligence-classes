'''
Ler largura, altura e apresentar o volume.
Volume = comprimento * largura * altura
Criar funções para este processo.
'''

comprimento = 0
largura = 0
altura = 0
volume = 0

def entradaDados():
    print("Digite o comprimento: ")
    global comprimento
    comprimento = float(input())
    #
    print("Digite a largura: ")
    global largura
    largura = float(input())
    #
    print("Digite a altura: ")
    global altura
    altura = float(input())

# end

def calculos(c, l, a):
    global volume
    volume = c * l * a
# end

def result(v):
    print(f"O Volume apurado é: {v}")
# end


if __name__ == '__main__':
    entradaDados()
    calculos(comprimento, largura, altura)
    result(volume)
