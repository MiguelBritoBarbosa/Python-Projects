def digitenumero(mensagem):
    while True:
        n = input(mensagem)
        try:
            n = int(n)
            return n
            break
        except:
            print("Número digitado inválido!")
            continue

n = digitenumero("digite um número: ")
print(f"O número digitado foi {n}")
