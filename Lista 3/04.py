def teste(num):
    try:
        num = float(num)
        return True
    except:
        return False

def area(*dados):
    Aquarto = dados[0]["Largura"] * dados[0]["Comprimento"]
    Asala = dados[1]["Largura"] * dados[1]["Comprimento"]
    Acozinha = dados[2]["Largura"] * dados[2]["Comprimento"]
    Abanheiro = dados[3]["Largura"] * dados[3]["Comprimento"]
    Casa = Aquarto + Asala + Acozinha + Abanheiro
    print(f"A área do quarto é {Aquarto}m²")
    print(f"A área da sala é {Asala}m²")
    print(f"A área da cozinha é {Acozinha}m²")
    print(f"A área do banheiro é {Abanheiro}m²")
    print(f"A área total do imóvel é {Casa}m²")

print("Digite as medidas do quarto")
quarto = {}
quarto["Cômodo"] = "quarto"
largura = input("Digite a largura do cômodo: ")
while teste(largura) == False or float(largura) < 1:
    largura = input("Digite uma largura válida!\n")
quarto["Largura"] = float(largura)
comprimento = input("Digite o comprimento do cômodo:")
while teste(comprimento) == False or float(comprimento) < 1:
    comprimento = input("Digite um comprimento válido!\n")
quarto["Comprimento"] = float(comprimento)

print("Digite as medidas da sala")
sala = {}
sala["Cômodo"] = "quarto"
largura = input("Digite a largura do cômodo: ")
while teste(largura) == False or float(largura) < 1:
    largura = input("Digite uma largura válida!\n")
sala["Largura"] = float(largura)
comprimento = input("Digite o comprimento do cômodo:")
while teste(comprimento) == False or float(comprimento) < 1:
    comprimento = input("Digite um comprimento válido!\n")
sala["Comprimento"] = float(comprimento)

print("Digite as medidas da cozinha")
cozinha = {}
cozinha["Cômodo"] = "quarto"
largura = input("Digite a largura do cômodo: ")
while teste(largura) == False or float(largura) < 1:
    largura = input("Digite uma largura válida!\n")
cozinha["Largura"] = float(largura)
comprimento = input("Digite o comprimento do cômodo:")
while teste(comprimento) == False or float(comprimento) < 1:
    comprimento = input("Digite um comprimento válido!\n")
cozinha["Comprimento"] = float(comprimento)

print("Digite as medidas do banheiro")
banheiro = {}
banheiro["Cômodo"] = "quarto"
largura = input("Digite a largura do cômodo: ")
while teste(largura) == False or float(largura) < 1:
    largura = input("Digite uma largura válida!\n")
banheiro["Largura"] = float(largura)
comprimento = input("Digite o comprimento do cômodo:")
while teste(comprimento) == False or float(comprimento) < 1:
    comprimento = input("Digite um comprimento válido!\n")
banheiro["Comprimento"] = float(comprimento)

area(quarto, sala, cozinha, banheiro)
