from random import randint
def numeros(num):
    try:
        int(num)
        return True
    except:
        pass
    return False

def nota(num):
    try:
        float(num)
        return True
    except:
        pass
    return False

def search(matriculas,matricula):
    try:
        i = matriculas.index(matricula)
        return i
    except:
        i = -1
        return i



escola = []
aluno = []
matriculas = []
teste = 0
i = -1
alunos = 0
while True:
    nome = input("Digite seu nome: ")
    aluno.append(nome)
    matricula = input("Digite sua mátricula: ")
    while numeros(matricula) == False or int(matricula) < 1:
        matricula = input("Digite uma matricula válida: ")
    matricula = int(matricula)
    if teste == 1 and matricula == escola[i][1]:
        print("Aluno já informado! Digite um novo aluno -> \n")
        aluno.clear()
        continue
    teste = 1
    aluno.append(matricula)
    matriculas.append(matricula)
    nota1 = input("Digite a primeira nota do bimestre: ")
    while nota(nota1) == False or float(nota1) < 1 or float(nota1) > 10:
        nota1 = input("Digite uma nota válida: ")
    nota1 = float(nota1)
    aluno.append(nota1)
    nota2 = input("Digite a segunda nota do bimestre: ")
    while nota(nota2) == False or float(nota2) < 1 or float(nota2) > 10:
        nota2 = input("Digite uma nota válida: ")
    nota2 = float(nota2)
    aluno.append(nota2)
    resp = input("Deseja adicionar outro aluno? (sim/não)")
    while resp != "sim" and resp != "não":
        resp = input("Digite uma resposta válida: ")
    escola.append(aluno[:])
    aluno.clear()
    i += 1
    alunos += 1
    if resp == "não":
        break

print("Os alunos inseridos foram -> ")

for i in range(len(escola)):
    print(f"{i+1}° aluno: {escola[i][0]}, mátricula: {escola[i][1]}, 1° nota: {escola[i][2]}, 2° nota: {escola[i][3]}")

matricula = input("\nEscolha um aluno atráves da matricula para calcular a média do bimestre: ")

while numeros(matricula) == False:
    matricula = input("Digite um número de mátricula válido: ")
matricula = int(matricula)

while search(matriculas, matricula) == -1:
    matricula = input("Digite uma mátricula válida: ")
    while numeros(matricula) == False:
        matricula = input("Digite um número de mátricula válido: ")
    matricula = int(matricula)

media = 0

for i in range(len(escola)):
    if escola[i][1] == matricula:
        media = (escola[i][2] + escola[i][3]) / 2
        print(f"A média do aluno: {escola[i][0]} no bimestre é {media} ")
        break
