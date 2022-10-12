def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False
from random import randint

palpites = []
jogo = []
x = input("Digite quantos jogos da mega-sena deseja simular: ")
while numeros(x) == False:
    x = input("Digite um número válido: ")
x = int(x)

for i in range(0,x):
    for i2 in range(0,6):
        num = randint(1,60)
        jogo.append(num)
        while jogo.count(num) > 1:
            jogo.pop()
            num = randint(1,60)
            jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()

for i in range(len(palpites)):
    print(f"{i+1}° jogo gerado: {palpites[i]}")
