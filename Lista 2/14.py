def numeros(num):
    try:
        float(num)
        return True
    except:
        pass
    return False

print("Crie uma lista com números diferentes ->")
print("(para encerrar a criação da lista digite 0)")
nums = []
while True:
    x = input("Digite um número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    x = float(x)
    if x == 0:
        break
    nums.append(x)
    while nums.count(x) > 1:
        nums.pop()
        x = input("Digite um valor diferente dos anteriores: ")
        while numeros(x) == False:
            x = input("Digite um número válido: ")
        x = float(x)
        if x == 0:
            print("Se deseja encerrar digite 0 novamente: ")
            break
        nums.append(x)

if len(nums) == 0:
    print("Não foi digitado nenhum número!")
else:
    print(nums)
