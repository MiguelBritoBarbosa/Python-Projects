nomeArquivo = input("Digite o nome do arquivo: ")
while nomeArquivo == "":
    nomeArquivo = input("Digite um nome de arquivo válido!\n")

textoArquivo = input("Digite o texto do arquivo: ")
while textoArquivo == "":
    textoArquivo = input("Digite um texto válido!\n")

arquivo = open(f"{nomeArquivo}.html", "w")
arquivo.write(textoArquivo)
arquivo.close()
