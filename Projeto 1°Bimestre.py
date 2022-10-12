
# Miguel Brito Barbosa, Lucas de Oliveira Maia, Agnes Vithória Santos bakos 2° FID

totalampadas = float()

while True:
    print("Quarto(1)\n"
          "Sala de TV(2)\n"
          "Salas(3)\n"
          "Cozinha(4)\n"
          "Varandas(5)\n"
          "Escritório(6)\n"
          "Banheiro(7)")
    nome = int(input("Digite o número do cômodo desejado:"))
    while nome < 1 or nome > 7:
        nome = int(input("Digite um cômodo válido!\n"))
    if nome == 1 or nome == 2:
        classe = 1
    elif nome == 3 or nome == 4 or nome == 5:
        classe = 2
    else:
        classe = 3

    largura = float(input(f"Digite a largura do cômodo em metros:"))
    while largura <= 0:
        largura = float(input(f"Digite uma largura válida!\n"))

    comprimento = float(input(f"Digite o comprimento do cômodo em metros:"))
    while comprimento <= 0:
        comprimento = float(input(f"Digite um comprimento válido\n"))

    area = largura * comprimento
    if classe == 1:
        potencia = area * 15
    elif classe == 2:
        potencia = area * 18
    else:
        potencia = area * 20
    lampadas = potencia/60
    aux = int(lampadas)
    if (lampadas - aux) != 0:
        aux += 1
        lampadas = aux
    totalampadas += lampadas
    totalwats = totalampadas * 60

    if nome == 1:
        print(f"A área do quarto é {area:.1f}m², a potência por m² necessária é 15W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    elif nome == 2:
        print(f"A área da sala de TV é {area:.1f}m², a potência por m² necessária é 15W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    elif nome == 3:
        print(f"A área da sala é {area:.1f}m², a potência por m² necessária é 18W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    elif nome == 4:
        print(f"A área da cozinha é {area:.1f}m², a potência por m² necessária é 18W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    elif nome == 5:
        print(f"A área da varanda é {area:.1f}m², a potência por m² necessária é 18W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    elif nome == 6:
        print(f"A área do escritório é {area:.1f}m², a potência por m² necessária é 20W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")
    else:
        print(f"A área do banheiro é {area:.1f}m², a potência por m² necessária é 20W,"
              f"para isso são necessárias {lampadas:.0f} lampadas")

    resp = input("Deseja adicionar mais cômodos S/N:").upper()
    while resp != "S" and resp != "N":
        resp = input("Digite uma resposta válida!\n")
    if resp == "N":
        break


valor = float(input("Digite o valor das lampadas:"))
while valor <= 0:
    valor = float(input("Digite um valor válido!\n"))

print(f"Para casa serão necessárais {totalampadas:.0f} lampadas")
print(f"O que dá um total de {totalwats:.0f} Watts")