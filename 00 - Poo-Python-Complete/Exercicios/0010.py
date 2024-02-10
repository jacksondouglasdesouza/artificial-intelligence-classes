'''

Leia os valores fornecido pelo usuário de:
COMPRIMENTO | LARGURA e ALTURA
em seguida forneça ao mesmo o valor do volume no console.
Ao final do processo, pérgunte ao usuário se ele deseja realizar uma nova operação!

'''

comprimento = 0
largura = 0
altura = 0
volume = 0
continuar = 's'

while continuar == 's' or continuar == "S":
    print("Digite aqui o valor para comprimento: ")
    comprimento = float(input())
    print("Digite aqui o valor para largura: ")
    largura = float(input())
    print("Digite aqui o valor para altura: ")
    altura = float(input())

    volume = comprimento * largura * altura

    print("\n**************************************************")
    print(f" volume para os dados informados é: {volume}")
    print("**************************************************n\n")

    print("Você deseja fazer uma nova operação? \n"
          "[ s ] - SIM\n"
          "[ n ] - NÃO")
    continuar = input()

print("\nPROGRAMA FINALIZADO!")