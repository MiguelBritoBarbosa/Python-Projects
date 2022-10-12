def numeros(num):
    try:
        float(num)
        num = float(num)
        if num > 1 and num < 10:
            return True
    except:
        pass
    return False

aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
media = input("Digite a média do aluno: ")
while numeros(media) == False:
    media = input("Digite uma média válida: ")
media = float(media)

aluno["média"] = media

if aluno["média"] <= 5.9:
    print("O aluno está de recuperação!")
else:
    print("Aluno está na média!")
