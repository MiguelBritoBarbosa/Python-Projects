def teste(num):
    try:
        num = int(num)
        return True
    except:
        return False

def primo(a):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                print(a, 'não é primo')
                break
        else:
            print(a, 'é primo')
    elif a == 0:
            print(a, 'é zero')
    elif a == 1:
        print(a, 'é um')
    else:
        print(a, 'é negativo')


x = input("Digite um número inteiro: ")
while teste(x) == False:
    x = input("Digite um número válido!\n")

primo(int(x))
