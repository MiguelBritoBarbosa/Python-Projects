print("Digite 5 números inteiro entre 0 e 10->")
nums = []
for i in range(0,5):
    x = input(f"Digite {i+1}° número: ")
    while (not x.isnumeric()) or int(x) < 0 or int(x) > 10:
        x = input("Digite um número válido: ")
    int(x)
    nums.append(x)

nums = tuple(nums)

#a)
a = nums.count("10")
print(f"\nO número 10 aparece {a} vez(es)")

#b)

b = "".join(nums)
b = b.find("3")

if b != -1:
    print(f"\nO número 3 foi o {b+1}° digitado")
else:
    print(f"\nNão foi digitado o número 3")

#c)
print("\nos números pares digitados foram: ")
for i in range(len(nums)):
    if int(nums[i]) % 2 == 0:
        print(f"{nums[i]}", end=" ")
