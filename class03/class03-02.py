def entradaDados(messenger):
    print(messenger)
    valueEntrada = float(input())
    return valueEntrada
# end

def somatoria(value1, value2):
    return value1 + value2
# end

def result(soma):
    print(f"O resultado é: {soma}")
# end

if __name__ == '__main__':
    value01 = entradaDados("Digite o primeiro Valor: ")
    value02 = entradaDados("Digite o segundo valor: ")
    soma = somatoria(value01, value02)
    result(soma)


