import datetime

def idade(num):
    try:
        int(num)
        num = int(num)
        if num > 1959 and num < 2007:
            return True
    except:
        pass
    return False

def trabalho(num, ano, hoje):
    try:
        int(num)
        num = int(num)
        if num > (int(ano) + 16) and num <= hoje:
            return True
    except:
        pass
    return False

trabalhador = {}

trabalhador["nome"] = input("Digite o nome do trabalhador: ")

ano = input("Digite o ano de nascimento: ")
while idade(ano) == False:
    ano = input("Digite uma idade válida para um trabalhador (mínimo 16 anos/maxímo 62): ")
hoje = datetime.date.today()
hoje = int(hoje.strftime("%Y"))
trabalhador["idade"] = hoje - int(ano)

carreira = input("Digite a data que iniciou sua carreira: ")
while trabalho(carreira, ano, hoje) == False:
    carreira = input("Digite um ano válido de inicio de carreira (pelo menos 16 anos): ")
trabalhador["carreira"] = hoje - int(carreira)
aposentar = 30 - trabalhador["carreira"]

print(f"O trabalhador", trabalhador["nome"], "tem", trabalhador["carreira"], f" anos de carreira e faltam {aposentar} anos para se aposentar")
