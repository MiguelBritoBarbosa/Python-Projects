print('Calculo para saber a quantidade de combustivel gasta em uma viagem')
x = (float(input('Quantas horas durou a viagem?')))
y = (float(input('Qual foi a velocidade média?')))
distancia = x * y
litros = distancia/12
print(f'A viagem demorou {x} horas, foi percorrido {distancia}km, foi gasto {litros:.1f}L')
