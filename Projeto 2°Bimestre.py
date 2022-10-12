#Projeto 2°Bimestre Miguel Brito Barbosa - Lucas de Oliveira Maia - Agnes Santos Bakos

cpf = []
CPFS = []
validos = 0
invalidos = 0
while True:

    dicionario = {}
    cpf.clear()
    x = input("Digite o cpf (com apenas números): ")
    while x.isnumeric() == False or len(x) != 11:
        x = input("Digite um cpf válido! ")

    for i in range(len(x)):
        if x[i].isnumeric():
            cpf.append(x[i])
    x = "".join(cpf)
    cpf.clear()

    for i in range(0,9):
        cpf.append(int(x[i]))

    teste = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    res = 0
    for i in range(len(cpf)):
        res += cpf[i] * teste[i]
    if res % 11 < 2:
        cpf.append(0)
    else:
        cpf.append(11 - (res % 11))
    teste.insert(0,11)
    res = 0
    for i in range(len(cpf)):
        res += cpf[i] * teste[i]
    if res % 11 < 2:
        cpf.append(0)
    else:
        cpf.append(11 - (res % 11))
    y = []
    for i in range(len(x)):
        y.append(int(x[i]))
    dicionario["cpf"] = y
    if y == cpf and cpf[9] != cpf[10]:
        dicionario["validação"] = "VÁLIDO"
        validos += 1
    else:
        dicionario["validação"] = "INVÁLIDO"
        invalidos += 1

    CPFS.append(dicionario)

    resp = input("Deseja inserir outro cfp? (sim/não): ")
    while resp != "sim" and resp != "não":
        resp = input("Digite um resposta válida! ")
    if resp == "não":
        break

quantidade = len(CPFS)
if quantidade == 1:
    print(f"Ao todo foi testesdo {quantidade} cpf.", end=" ")
    if validos == 1:
        print("Esse cpf é válido.")
    else:
        print("Esse cpf é inválido.")

elif quantidade == 2:
    print(f"Ao todo foram testesdos {quantidade} cpfs.", end=" ")
    if validos == invalidos:
        print("Um foi válido e um inválido.")
    elif validos == 2:
        print("Os dois foram válidos.")
    else:
        print("Os dois foram inválidos.")

else:
    print(f"Ao todo foram testesdos {quantidade} cpfs.", end=" ")
    if validos == quantidade:
        print("Todos são válidos.")
    elif invalidos == quantidade:
        print("Todos são inválidos.")
    elif validos == 1:
        print(f"1 foi válidos e {invalidos} foram inválidos")
    elif invalidos == 1:
        print(f"{validos} foram válidos e 1 foi inválido")
    else:
        print(f"{validos} foram válidos e {invalidos} foram inválidos.")

validos = (validos * 100) / quantidade
invalidos = (invalidos * 100) / quantidade

print(f"A porcentagem de válidos é de {validos:.1f}% e de inválidos é de {invalidos:.1f}%.")
for i in range(len(CPFS)):
    print(CPFS[i])