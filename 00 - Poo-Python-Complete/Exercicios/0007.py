'''

Apresente no console o valor do acumulado da soma dos 100
primeiros números inteiros executados no contador i

'''

i = 0
soma = 0

while i < 101:
    soma += i
    i += 1

print(soma)