def Inteiro(num):
    try:
        num = int(num)
        return True
    except:
        return  False


def Real(num):
    try:
        num = float(num)
        return True
    except:
        return False


x = input("Digite um número inteiro: ")
while Inteiro(x) == False:
    x = input("Digite um número inteiro!\n")

x = input("Digite um número real: ")
while Real(x) == False:
    x = input("Digite um número real!!\n")

print("-"*10, "Fim da execução do program", "-"*10)
