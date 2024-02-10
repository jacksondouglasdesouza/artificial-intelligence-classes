'''

leia as informaç~eos de um corcórcio como:
Total de prestações
prestações pagas
valor de cada prestação

Mostre o valor pago total e o saldo devedor

'''


print("Digite o total de prestações: ")
totalPrestacoes = float(input())

print("Digite quantas foram pagas: ")
totalPagas = float(input())

print("Digite  valor de cada prestação :")
valorPrestacao = float(input())

valorDivida = totalPrestacoes * valorPrestacao
valorPago = totalPagas * valorPrestacao
valorDevedor = valorDivida - valorPago

print("************")
print("O valor do contrato é de: ", valorDivida)
print("O valor pago foi de: ", valorPago)
print("A sua dívida e de: ", valorDevedor)


