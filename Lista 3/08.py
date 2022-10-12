def teste(num):
    try:
        num = int(num)
        if num > 0:
            return True
        else:
            return False
    except:
        return False

def pessoa(pessoa = "", MaiorMenor = -1):
    if pessoa != "":
        print(f"Seu nome é {pessoa}.", end=" ")
    else:
        print("Nome não informado.", end=" ")
    if MaiorMenor != -1 and MaiorMenor >= 18:
        print("Você é maior de idade.")
    elif MaiorMenor != -1 and MaiorMenor < 18:
        print("Você é menor de idade.")
    else:
        print("Idade não informada.")

resp1 = input("Deseja digitar seu nome? (s/n): ")
while resp1 != "s" and resp1 != "n":
    resp1 = input("Digite uma resposta válida!\n")
if resp1 == "s":
    nome = input("Digite seu nome: ")

resp2 = input("Deseja digitar sua idade? (s/n): ")
while resp2 != "s" and resp2 != "n":
    resp2 = input("Digite uma resposta válida!\n")
if resp2 == "s":
    idade = input("Digite sua idade: ")
    while teste(idade) == False:
        idade = input("Digite uma idade válida!\n")
    idade = int(idade)
if resp1 == "s" and resp2 == "s":
    pessoa(nome,idade)
elif resp1 == "s" and resp2 == "n":
    pessoa(nome)
elif resp1 == "n" and resp2 == "s":
    pessoa(MaiorMenor=idade)
else:
    pessoa()
