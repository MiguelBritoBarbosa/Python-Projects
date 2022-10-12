nome = input("Digite seu nome: ").lower()
nome = nome.split()
for i in range(len(nome)):
    x = nome[i]
    if x == "silva":
        resp = True
        break
    else:
        resp = False
print(resp)
