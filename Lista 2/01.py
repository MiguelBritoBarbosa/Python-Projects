frase = input("Digite uma frase: ")
#a)
print(f"Frase em letras maiúsculas: {frase.upper()}")
#b)
print(f"Frase em letras minúsculas: {frase.lower()}")
#c)
x = frase.split()
frase = "".join(x)
print(f"Quantas letras tem na frase: {len(frase)}")
#d)
print(f"A primeira palavra da frase tem: {len(x[0])}") 
