'''

12km por litro
tempo viagem
velocidade média

Distancia = tempo * velocidade
litrosUsados = Distancia / 12

'''

print("Digite o tempo da viagem: ")
tempo = float(input())

print("Digite a velocidade média: ")
velocidade = float(input())

distancia = tempo * velocidade
litros = distancia / 12


print("A velocidade média é: ", velocidade)
print("O tempo gasto é: ", tempo)
print("A distância percorrida: ", distancia)
print("Litros de combustível gasto: ", litros)