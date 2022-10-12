def numeros(num):
    try:
        float(num)
        return True
    except:
        pass
    return False

funcionarios = []
pessoa = ["", 0]
totalpessoas = 1;
while True:
    pessoa[0] = input("Digite seu nome: ")
    pessoa[1] = input("Digite seu salário: ")
    while numeros(pessoa[1]) == False or float(pessoa[1]) <= 0:
        pessoa[1] = input("Digite um salario válido: ")
    pessoa[1] = float(pessoa[1])
    funcionarios.append(pessoa[:])

    resp = input("Digite se deseja encerrar a criação da lista?(sim/não): ")
    resp = resp.lower()
    while resp != "sim" and resp != "não":
        resp = input("Digite a resposta novamente: ")
    if resp == "sim":
        break
    else:
        totalpessoas += 1

print(f"Lista -> {funcionarios}")

#a)
totalsalarios = 0
for i , salario in enumerate(funcionarios):
    totalsalarios += salario[1]
print(f"A soma de todos os salários é = {totalsalarios}")

#b)
print(f"O total de pessoas inscritas na lista é = {totalpessoas}")

#c)
print(f"O menor salário digitado foi {min(funcionarios)[1]}")
