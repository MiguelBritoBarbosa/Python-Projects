def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

nums = []
print("Crie uma lista de 8 números inteiros ->\n")
for i in range(0,8):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input(f"Digite um número válido: ")
    x = int(x)
    nums.append(x)
    while nums.count(x) > 1:
        nums.pop()
        x = input("Digite um valor diferente dos anteriores: ")
        while numeros(x) == False:
            x = input("Digite um número válido: ")
        x = int(x)
        nums.append(x)
    for i in range(len(nums) - 1, 0, -1):
        for c in range(i):
            if nums[c] < nums[c + 1]:
                aux = nums[c]
                nums[c] = nums[c + 1]
                nums[c + 1] = aux
    print(f"O número digitado foi inserido na {nums.index(x) + 1}°posição\n")
numsPares = []
numsImpares = []
for i in range(0,8):
    if nums[i] % 2 == 0:
        numsPares.append(nums[i])
    else:
        numsImpares.append(nums[i])
print(nums)
print(f"A lista de números pares ficou: {numsPares}")
print(f"A lista de número impares ficou: {numsImpares}")
