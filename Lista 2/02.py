x = input("digite um número inteiro e positivo: ")
while not(x.isnumeric()):
    x = input("digite um número válido: ")
x = float(x)
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
um = x // 1000 % 10

print(f"O número digitado tem {um:.0f} unidades de milhar, {c:.0f} centenas, {d:.0f} dezenas e {u:.0f} unidades")
