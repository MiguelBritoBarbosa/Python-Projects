def binario():
    try:
        x = float(num)
        if x % 1:
            numero = num.split(".")
            numero[0] = format(int(numero[0]), "b")
            numero[1] = format(int(numero[1]), "b")
            print(f"O número {x} em binário fica {numero[0]}.{numero[1]}")
        else:
            print(f"O número {x:.0f} em binário fica {format(int(num), 'b')}")
    except:
        print("O número digitado é inválido!")


num = input("Digite um número decimal ou inteiro: ")
binario()
