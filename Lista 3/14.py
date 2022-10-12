def numero(num):
    try:
        num = float(num)
        return True
    except:
        return False

def calculo(tipo, x):
    if tipo == 1:
        res = x**2
        return res
    elif tipo == 2:
        if x > 0:
            res = x**(1/3)
        else:
            res = "Não existe raiz de número negativo"
        return res
    else:
        if x < 0:
            print("Não existe fatorial negativo")
        elif x == 0:
            return 1
        else:
            fact = 1
            while (x > 1):
                fact *= x
                x -= 1
            return fact


print("-"*50)
print(f"{'1- QUADRADO DE UM NÚMERO':^50}")
print(f"{'2- RAIZ CÚBICA DE UM NÚMERO ':^50}")
print(f"{'3- FATORIAL DE UM NÚMERO':^50}")
print("-"*50)

resp = input()
while numero(resp) == False or int(resp) > 3 or int(resp) < 1:
    resp = input("Digite uma opção existente!\n")
resp = int(resp)

x = input("Digite um número: ")
while numero(x) == False:
    x = input("Digite um número válido")
x = float(x)

x = calculo(resp, x)

print(f"Resultado: ", x)
