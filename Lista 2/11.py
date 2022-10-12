print("-"*32)
print(f"{'LISTAGEM DE PREÇOS': ^32}")
print("-"*32)

preços = ("lápis", "Borracha", "Caderno", "Estojo", "Transferidor", "Compasso", "Mochila", "Canetas", "Livro",
          "1.75", "2.00", "15.90", "25.00", "4.20", "9.99", "120.32", "22.30", "34.90")

for i in range(0, 9):
    print(preços[i], end="")
    if i == 4:
        print("."*10, end="")
    elif i == 1:
        print("." * 14, end="")
    elif i == 2:
        print("." * 15, end="")
    elif i == 3:
        print("." * 16, end="")
    elif i == 5:
        print("." * 14, end="")
    elif i == 6:
        print("." * 15, end="")
    elif i == 7:
        print("." * 15, end="")
    else:
        print("."*17, end="")

    print("R$",f"{preços[i+9]: >6}")

print("-"*32)
