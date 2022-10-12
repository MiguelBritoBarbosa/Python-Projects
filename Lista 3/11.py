def ValidarCPF(cpf):
    cpfTeste = []

    for i in range(0, 9):
        cpfTeste.append(int(cpf[i]))

    teste = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    res = 0
    for i in range(len(cpfTeste)):
        res += cpfTeste[i] * teste[i]
    if res % 11 < 2:
        cpfTeste.append(0)
    else:
        cpfTeste.append(11 - (res % 11))
    teste.insert(0, 11)
    res = 0
    for i in range(len(cpfTeste)):
        res += cpfTeste[i] * teste[i]
    if res % 11 < 2:
        cpfTeste.append(0)
    else:
        cpfTeste.append(11 - (res % 11))

    if cpf == cpfTeste and cpfTeste[9] != cpfTeste[10]:
        return "CPF VÁLIDO"
    else:
        return "CPF INVÁLIDO"
