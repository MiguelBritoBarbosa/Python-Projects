from random import randint
sorteio = {}
jogadores = []
numeros = []
for i in range(0,4):
    jogador = input(f"Digite o {i+1}° jogador: ")
    jogadores.append(jogador)
    while i != 0 and jogadores.count(jogador) > 1:
        jogadores.pop()
        jogador = input("Digite um novo jogador! -> ")
        jogadores.append(jogador)
sorteio["jogadores"] = jogadores[:]
for i in range(0,4):
    numeros.append(randint(1,6))
    while i != 0 and numeros.count(numeros[i]) > 1:
        numeros.pop()
        numeros.append(randint(1,6))

sorteio["números"] = numeros[:]

print("Valores sorteados: ")
for i in range(0,4):
    print(f"  O jogador", sorteio["jogadores"][i], "tirou", sorteio["números"][i])

print("O ranking dos jogadores ficou: ")

posições = []
for i in range(0,4):
    posições.append(numeros.index(max(numeros)))
    numeros[numeros.index(max(numeros))] = -1
numeros = sorted(sorteio["números"], reverse=True)

for i in range(0,4):
    print(f"  {i+1}° lugar: ", end="")
    for y in range(0,4):
        if y == posições[i]:
            print(sorteio["jogadores"][y], f"com {numeros[i]}")
