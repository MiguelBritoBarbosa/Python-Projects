def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False



time = {}

time["time"] = input("Digite o nome do seu time: ")

x = input("Digite quantas partidas o time jogou: ")
while numeros(x) == False or int(x) < 1:
    x = input("Digite um número válido de partidas: ")
x = int(x)
gols = []
for i in range(0,x):
    gol = input(f"Digite quantos gols foram feitos na {i+1}° partida: ")
    while numeros(gol) == False or int(gol) < 0:
        gol = input("Digite um número válido de gols: ")
    gol = int(gol)
    gols.append(gol)
time["gols por partida"] = gols[:]
total = 0
for i in range(len(gols)):
    total += gols[i]
time["total de gols"] = total

print("\no time informado foi", time["time"], f"que disputou {x} e fez os seguintes gols: ")

for i in range(len(gols)):
    print(f"{'Partida': >20} {i+1}: {time['gols por partida'][i]} ")
print(f"{'Total de gols ===>': >27} {time['total de gols']}")
