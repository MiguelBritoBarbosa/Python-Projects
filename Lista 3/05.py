def teste(num):
    try:
        num = float(num)
        return True
    except:
        return False

def MaiorMenor(lista):
    maior = max(lista)
    menor = min(lista)
    print(f"O maior número digitado foi {maior} que está na posição {lista.index(maior)}")
    print(f"O menor número digitado foi {menor} que está na posição {lista.index(menor)}")

numeros = []
while True:
    while True:
        x = input("Digite um número: ")
        while teste(x) == False:
            x = input("Digite um número válido!\n")
        numeros.append(float(x))
        if numeros.count(float(x)) > 1:
            numeros.pop()
            print("Este número já foi digitado!")
            continue
        break

    resp = input("Deseja adicionar mais números? (s/n)\n")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!\n")
    if resp == "n":
        break

MaiorMenor(numeros)
