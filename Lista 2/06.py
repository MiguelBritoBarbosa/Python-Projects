nome = input("Digite seu nome: ")
nome = nome.split()
x = "".join(nome)
while not x.isalpha():
    nome = input("Digite um nome válido! ")
    nome = nome.split()
    x = "".join(nome)

for x in range(len(nome)):
    x = nome[x]

print(f"Seu primeiro nome é {nome[0]} e o ultimo é {x}")
