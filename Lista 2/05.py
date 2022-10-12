nome = input("Digite seu nome: ")
x = nome.split()
x = "".join(x)
while not(x.isalpha()):
    nome = input("Digite um nome válido! ")
    x = nome.split()
    x = "".join(x)
#a)
x = nome.upper().count("A")
print(f"No seu nome tem {x} letras 'a' (com exceção de acentos)")

#b)
y = nome.upper().find("A")
if y != -1:
    print(f"A primeira vez que aparece a letra 'a' no seu nome é na posição {y}")
else:
    print("Não a letras 'a' nesse nome")

#c)
z = nome.upper().rindex("A")

if z != -1:
    print(f"A ultima vez que aparece a letra 'a' no seu nome é na posição {z}")
else:
    print("Não letras 'a' nesse nome")
