'''

Leia a idade do usuário e classifique-a em:
Criança se > idade entre 0 e 12
Adolescente se > idade entre 13 e 17
adulto se > idade acima de 18 anos
caso caracteres inválidos e negativos informa ao usuário
mensagem de dado inserido inválido.

'''

print("Digite aqui a sua idade: ")
value = input()

if value.isdigit():
    idade = int(value)

    if idade >= 18:
        print(f"A sua idade é {idade}, você já é um adulto!")
    elif idade >= 13 and idade <= 17:
        print(f"Sua idade é {idade}, você ainda é um adolescente!")
    else:
        print(f"Sua idade é {idade}, você ainda é um criança")
else:
    print("Digite um carácter válido! Este valor não é válido para idade!")