def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

matriz = []
vetor1 = []
vetor2 = []
vetor3 = []
print("Crie uma matriz 3x3 com números inteiros: ")

for i in range(0,3):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    int(x)
    vetor1.append(x)

for i in range(3,6):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    int(x)
    vetor2.append(x)


for i in range(6,9):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    int(x)
    vetor3.append(x)


matriz.append(vetor1)
matriz.append(vetor2)
matriz.append(vetor3)

print(matriz)

print("A matriz feita ficou ->")
for l, c in enumerate(matriz):
    print("\n")
    for i, v in enumerate(c):
        print(f"{v: ^5}", end=" ")
