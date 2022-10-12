sm = (float(input('Digite o valor do sálario')))
pr = (float(input('Digite o percentual de reajuste')))
ns = sm + (sm*(pr/100))
print(f'O novo salário é = R${ns:.2f}')
