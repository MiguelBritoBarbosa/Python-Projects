numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")

n = input("digite um número inteiro entre 0 e 10: ")
while not(n.isnumeric()) or int(n) < 0 or int(n) > 10:
    n = input("Digite um número válido: ")
n = int(n)
print(f"o número digitado foi {numeros[n]}")
