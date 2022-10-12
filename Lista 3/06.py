def teste(num):
    try:
        num = float(num)
        return True
    except:
        return False

def media(media):
    mensagem = ""
    if media >= 6:
        mensagem = "Aluno aprovado!"
    elif media < 6 and media > 3.5:
        mensagem = "Aluno em exame!"
    else:
        mensagem = "Aluno reprovado!"
    return mensagem

while True:
    nota = input("Digite a nota do aluno: ")
    while teste(nota) == False or float(nota) < 0:
        nota = input("Digite uma nota válida!\n")
    print(media(float(nota)))
    resp = input("Deseja testar outra nota?(s/n)\n")
    while resp != "s" and resp != "n":
        resp = input("Digite uma respota válida!\n")
    if resp == "n":
        break
