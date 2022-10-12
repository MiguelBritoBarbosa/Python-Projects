def teste(num):
    try:
        num = int(num)
        return True
    except:
        return False

def soma(num, resp):
    '''
    Está rotina soma todos os números antecessores ao número digitado pelo usuário.
    Que pode ou não demonstrar o processor de soma
    :param num: Este parâmetro é um número digitado pelo usuário
    :param resp: Este parâmetro é a resposta do usuário para a opção de mostrar ou não o processo da soma
    :return mensagem: Será retornado ao módulo principal do programa a mensagem com ou sem o processo da soma
    '''
    res = 0
    mensagem = "Soma = "
    for i in range(0,num+1):
        res += i
        if resp == "s" and res > 0:
            mensagem += str(i)
            if i == num:
                mensagem += " = "
            else:
                mensagem += "+"

    mensagem += str(res)
    print(res)
    return mensagem


while True:
    x = input("Digite um número inteiro positivo: ")
    while teste(x) == False or int(x) < 0:
        x = input("Digite um número válido\n")
    resp = input("Deseja visualizar o processo da soma? (s/n): ")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!\n")
    x = int(x)
    print(soma(x,resp))
    resp = input("Deseja inserir outro número? (s/n): ")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!\n")
    if resp == "n":
        break
help(soma)
