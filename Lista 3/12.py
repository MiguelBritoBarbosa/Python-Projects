import teste

while True:
    cpf = []
    x = input("Digite o cpf (com apenas números): ")
    while x.isnumeric() == False or len(x) != 11:
        x = input("Digite um cpf válido! ")
    for i in range(0, 11):
        cpf.append(int(x[i]))
    print(teste.ValidarCPF(cpf))
    resp = input("Deseja testar outro cpf?(s/n)")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!\n")
    if resp == "n":
        break
