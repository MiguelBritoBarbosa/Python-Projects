times = ("Flamengo", "Corinthians", "São Paulo", "Vasco", "Palmeiras",
        "Internacional", "Bragantino", "Atlético Mineiro", "Botafogo", "Fluminense")
print(times)

time = input("Digite um time entre os 10 apresentados: ")
x = time.split()
x = "".join(x)
print(x)
while not(x.isalpha()) or (x != "Flamengo" and x != "Corinthians" and
    x != "SãoPaulo" and x != "Vasco" and x != "Palmeiras" and
    x != "Internacional" and x != "Bragantino" and x != "AtléticoMineiro"
    and x != "Botafogo" and x != "Fluminense"):

    time = input("Digite um time válido: ")
    x = time.split()
    x = "".join(x)

#a)
print("PRIMEIROS COLOCADOS:\n")
for i in range(0,5):
    x = times[i]
    print(f"O {i+1}° colocado é: {x}")

#b)
print("\nULTIMOS COLOCADOS: ")
for i in range(6,10):
    x = times[i]
    print(f"O {i+1}° colocado é {x}")

#c)
x = tuple(sorted(times))
print(f"\n Os times em ordem alfabética ficam:\n{x}")

#d)
print(f"O time digitado pelo usuário está na pósição {times.index(time) + 1}")
