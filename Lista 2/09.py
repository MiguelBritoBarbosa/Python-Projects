import time
from random import randint
from time import sleep

print("Gerando 5 números aleatórios entre 0 e 100...")
time.sleep(3)

nums = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = nums[1]
menor = nums[1]

for i in range(len(nums)):
    x = nums[i]
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
print(f"O maior número gerado foi {maior}, e o menor foi {menor}")

print(f"Os números sorteados foram: \n {nums}")
