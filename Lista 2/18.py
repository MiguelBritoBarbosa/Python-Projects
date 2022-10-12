def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

nums = []
pares = []
impares = []
print("Crie uma lista de 10 números ->")
for i in range(0,10):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    x = int(x)
    nums.append(x)
    if x % 2 == 0:
        pares.append(x)
        teste = 1
    else:
        impares.append(x)
        teste1 = 1
nums.append(sorted(pares))
nums.append(sorted(impares))

print(f"A lista criada foi {nums}")
if teste == 1:
    print(f"A lista em ordem crescente com apenas números pares é = {nums[10]}")
if teste1 == 1:
    print(f"A lista em ordem crescente com apenas números impares é = {nums[11]}")
