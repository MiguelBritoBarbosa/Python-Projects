cidade = input("Digite o nome da sua cidade: ")
x = cidade.split()
x[0] = x[0].lower()
if x[0] == "são":
    print("O nome da cidade se inicia com São")
else:
    print("O nome da cidade não se inicia com São")
