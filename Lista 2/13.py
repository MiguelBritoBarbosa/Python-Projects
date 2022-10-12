def numeros(num):
    try:
        float(num)
        return True
    except:
        pass
    return False
nums = []
print("Digite 5 números ->")
for i in range(0,5):
    x = input(f"Digite o {i+1}° número: ")
    while numeros(x) == False:
        x = input("Digite um número válido: ")
    x = float(x)
    nums.append(x)
maior = max(nums)
menor = min(nums)
if nums.count(maior) > 1:
    print(f"O maior número digitado foi {maior} nas posições: ", end="")
    y = nums.index(maior)
    for i in range(nums.count(maior)):
        p = nums.index(maior, y)
        y = p + 1
        print(f"{p+1}", end=" ")
else:
    print(f"O maior número digitado foi {maior} na {nums.index(maior)+1}° posição", end="")
if nums.count(menor) > 1:
    print(f"\n E o menor número digitado foi {menor} nas posições: ", end="")
    y = nums.index(menor)
    for i in range(nums.count(menor)):
        p = nums.index(menor, y)
        y = p + 1
        print(f"{p+1}", end=" ")
else:
    print(f"\ne o menor número digitado foi {menor} na {nums.index(menor)+1}° posição.")
