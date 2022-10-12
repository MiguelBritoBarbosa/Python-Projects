def numero(num):
    try:
        num = float(num)
        return True
    except:
        return False


def informações(faturamentos):
    total = 0
    maior = max(faturamentos)
    menor = min(faturamentos)
    for value in faturamentos:
        total += value
    media = total / len(faturamentos)
    comercio = {
        "Total faturamento": total,
        "Maior faturamento": maior,
        "Menor faturamento": menor,
        "Faturamento médio": round(media,2)
    }
    return comercio


faturamentos = []
while True:
    x = input("Digite o faturamento diário: ")
    while numero(x) == False:
        x = input("Digite um número válido!\n")
    x = float(x)
    faturamentos.append(x)
    resp = input("Deseja inserir outro faturamento?(s/n)")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!\n")
    if resp == "n":
        break

comercio = informações(faturamentos)

print(comercio)
