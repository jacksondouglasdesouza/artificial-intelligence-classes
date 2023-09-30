'''
Ler idade de entrada
criar função para distiguir entre:
criança: 0 a 12
adolescente: 13 a 17
adulto: acime de 18
adptar função para não aceitar entrada negativa.
'''

idade = 0

def entradaDados(messager):
    print(messager)
    global idade
    idade = int(input())
# end

def comparacao(valueIdade):
    if valueIdade  > 0 and valueIdade <= 12:
        print(f"Sua idade é {valueIdade} você ainda é uma criança!")
    elif valueIdade >= 13 and idade <= 17:
        print(f"Sua idade é {valueIdade} você ainda é adolescente!")
    elif valueIdade >= 18:
        print(f"Sua idade é {valueIdade} você é adulto!")
    else:
        print("O VALOR DIGITADO É INVÁLIDO!")
# end

if __name__ == '__main__':
    entradaDados("Digite a idade: ")
    comparacao(idade)

