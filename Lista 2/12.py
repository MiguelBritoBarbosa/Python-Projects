print("Digite 4 palavras ->")
palavras = [input("Digite a 1° palavra: "), input("Digite a 2° palavra: "),
            input("Digite a 3° palavra: "), input("Digite a 4° palavra: ")]


for i in range(len(palavras)):
    print(f"\nNa palavra {palavras[i]} temos as vogais", end=" ")
    for x in range(len(palavras[i])):
        if palavras[i][x] == "a" or palavras[i][x] == "e" or palavras[i][x] == "i" or palavras[i][x] == "o" or palavras[i][x] == "u"\
        or palavras[i][x] == "A" or palavras[i][x] == "E" or palavras[i][x] == "I" or palavras[i][x] == "O" or palavras[i][x] == "U":
            print(palavras[i][x], end=" ")        
