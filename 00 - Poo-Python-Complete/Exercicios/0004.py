'''

Leia dois números reais de uma operação
imprima no console o resultado da operação
de acordo com a operação aritmética escolhida
pelo usuário.
Mostrar operação inválida caso caracteres inválidos

'''

print("Dite o primeiro valor: ")
value01 = float(input())

print("Dite o segundo valor: ")
value02 = float(input())


print("Escolha a operação correspondente: "
      "\n"
      "[ + ] - ADIÇÃO \n"
      "[ - ] - SUBTRAÇÃO \n"
      "[ * ] - MULTIPLICAÇÃO \n"
      "[ / ] - DIVISÃO \n")
operacao = input()

if operacao in ("+", "-", "*", "/"):
        if operacao == "+":
            print(f"Você escolheu Adição: {operacao}")
            print(f"O valor de {value01} + {value02} = {value01 + value02}")
        elif operacao == "-":
            print(f"Você escolheu Subtração: {operacao}")
            print(f"O valor de {value01} - {value02} = {value01 - value02}")
        elif operacao == "*":
            print(f"Você escolheu Multiplicação: {operacao}")
            print(f"O valor de {value01} x {value02} = {value01 * value02}")
        elif operacao == "/":
            if value02 != 0:
                print(f"Você escolheu Divisão: {operacao}")
                print(f"O valor de {value01} / {value02} = {value01 / value02}")
            else:
                print("IMPOSSIVEL DIVIDIR POR ZERO!")
else:
    print("Esta operação escolhida é inválida!")