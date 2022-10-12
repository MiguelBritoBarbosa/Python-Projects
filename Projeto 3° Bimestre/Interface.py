import BancoDeDados
from colorama import Fore, Back

def numeros(num):
    try:
        num = int(num)
        return True
    except:
        return False

def VerificarTabela(IdTabela, tabela):
    for i in range(len(tabela)):
        if IdTabela == tabela[i][0]:
            return tabela[i][1]
    return -1

# MÓDULO PRINCIPAL DO PROGRAMA ----->

while True:
    NomeBancoDeDados = input(
        Back.BLACK + Fore.LIGHTWHITE_EX + "Digite o nome da base de dados que deseja acessar: ")

    teste = BancoDeDados.OpenDatabase(NomeBancoDeDados)
    if teste == 0:
        resp = input(f"Ouve um erro ao tentar conexão com o banco {NomeBancoDeDados}, deseja reescrever o nome do banco? (s/n)\n")
        resp = BancoDeDados.ValidarResposta(resp)
        if resp == "n":
            break
        else:
            continue
    break

if teste == 1:
    while True:

        print(Fore.GREEN + "-"*50)
        print(Fore.BLUE + f"{'C':>23}", end="")
        print(Fore.RED + "R", end="")
        print(Fore.YELLOW + "U", end="")
        print(Fore.MAGENTA+ "D" + Fore.RESET)
        print(Fore.GREEN + "-"*50)
        print(Fore.BLUE + f"{'• C (Create/insert) – Criar registros':^46}")
        print(Fore.RED + f"{'• R (Read/select) – Ler registros':^42}")
        print(Fore.YELLOW + f"{'• U (Update) – Atualizar/Alterar Registros':^50}")
        print(Fore.MAGENTA + f"{'• D (Delete) – Deletar/Excluir registros':^49}")
        print(Fore.GREEN + "-"*50 + Fore.RESET)

        Ação = input(Back.BLACK + Fore.LIGHTWHITE_EX + "Digite a letra referente ao tipo de ação que deseja realizar: ")
        while Ação != "C" and Ação != "R" and Ação != "U" and Ação != "D":
            Ação = input("Digite uma das letras acima!(C.R.U.D)\n")

        if Ação == "C":
            while True:
                while True:
                    grid, tabelas = BancoDeDados.Tables()
                    print(grid)
                    NomeTabela = input("Digite o número da tabela que deseja inserir um registro: ")
                    while numeros(NomeTabela) == False:
                        NomeTabela = input("Digite um número de tabela corretamente!\n")
                    NomeTabela = int(NomeTabela)
                    NomeTabela = VerificarTabela(NomeTabela,tabelas)
                    while NomeTabela == -1:
                        NomeTabela = input("Digite um número de tabela existente!\n")
                        while numeros(NomeTabela) == False:
                            NomeTabela = input("Digite um número de tabela corretamente!\n")
                        NomeTabela = int(NomeTabela)
                        NomeTabela = VerificarTabela(NomeTabela, tabelas)

                    teste = BancoDeDados.InsertTable(NomeTabela)
                    if teste == 0:
                        resp = input(f"Ouve um erro ao tentar executar o registro na tabela {NomeTabela}, Deseja tentar executar o registro novamente?(s/n)\n")
                        resp = BancoDeDados.ValidarResposta(resp)
                        if resp == "n":
                            break
                        else:
                            continue
                    else:
                        break
                resp = input("Deseja fazer outra inserção? (s/n)\n")
                resp = BancoDeDados.ValidarResposta(resp)
                if resp == "n":
                    break

        elif Ação == "R":
            while True:
                resp = input("Deseja consultar todos os registros ou 1 específico?\n 0 - Todos\n 1 - 1 específico\n")
                while resp != "0" and resp != "1":
                    resp = input("Digite uma resposta válida!(0/1)\n")

                if resp == "0":
                    while True:
                        grid, tabelas = BancoDeDados.Tables()
                        print(grid)
                        NomeTabela = input("Digite o número da tabela que deseja consultar todos os registros: ")
                        while numeros(NomeTabela) == False:
                            NomeTabela = input("Digite um número de tabela corretamente!\n")
                        NomeTabela = int(NomeTabela)
                        NomeTabela = VerificarTabela(NomeTabela,tabelas)
                        while NomeTabela == -1:
                            NomeTabela = input("Digite um número de tabela existente!\n")
                            while numeros(NomeTabela) == False:
                                NomeTabela = input("Digite um número de tabela corretamente!\n")
                            NomeTabela = int(NomeTabela)
                            NomeTabela = VerificarTabela(NomeTabela, tabelas)

                        teste = BancoDeDados.SelectALl(NomeTabela)
                        if teste == 0:
                            resp = input(f"Ouve um erro ao tentar consultar todos os registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                            resp = BancoDeDados.ValidarResposta(resp)
                            if resp == "n":
                                break
                            else:
                                continue
                        elif teste == 2:
                            resp = input(f"A tabela {NomeTabela} está vazia, deseja inserir um registro?(s/n)\n")
                            resp = BancoDeDados.ValidarResposta(resp)
                            if resp == "s":
                                teste = BancoDeDados.InsertTable(NomeTabela)
                                if teste == 0:
                                    resp = input(f"Ouve um erro ao tentar consultar 1 registro da tabela {NomeTabela},  deseja tentar novamente?(s/n)\n")
                                    resp = BancoDeDados.ValidarResposta(resp)
                                    if resp == "n":
                                        break
                                    else:
                                        continue
                                break
                            else:
                                break
                        else:
                            break
                else:
                    while True:
                        grid, tabelas = BancoDeDados.Tables()
                        print(grid)
                        NomeTabela = input("Digite o número da tabela que deseja consultar 1 registro: ")
                        while numeros(NomeTabela) == False:
                            NomeTabela = input("Digite um número de tabela corretamente!\n")
                        NomeTabela = int(NomeTabela)
                        NomeTabela = VerificarTabela(NomeTabela, tabelas)
                        while NomeTabela == -1:
                            NomeTabela = input("Digite um número de tabela existente!\n")
                            while numeros(NomeTabela) == False:
                                NomeTabela = input("Digite um número de tabela corretamente!\n")
                            NomeTabela = int(NomeTabela)
                            NomeTabela = VerificarTabela(NomeTabela, tabelas)

                        Id = input("Digite o Id do registro que deseja chamar: ")
                        while Id.isnumeric() == False or int(Id) <= 0:
                            Id = input("Digite um número válido: ")
                        teste = BancoDeDados.Select(NomeTabela, Id)
                        if teste == 0:
                            resp = input(f"Ouve um erro ao tentar consultar 1 registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                            resp = BancoDeDados.ValidarResposta(resp)
                            if resp == "n":
                                break
                            else:
                                continue
                        elif teste == 2:
                            resp = input(f"Esse registro não foi encontrado na tabela {NomeTabela}, deseja inserir um registro?(s/n)\n")
                            resp = BancoDeDados.ValidarResposta(resp)
                            if resp == "s":
                                teste = BancoDeDados.InsertTable(NomeTabela)
                                if teste == 0:
                                    resp = input(f"Ouve um erro ao tentar consultar 1 registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                                    resp = BancoDeDados.ValidarResposta(resp)
                                    if resp == "n":
                                        break
                                    else:
                                        continue
                                break
                            else:
                                break
                        else:
                            break

                resp = input("Deseja fazer uma consulta novamente? (s/n)\n")
                resp = BancoDeDados.ValidarResposta(resp)
                if resp == "n":
                    break

        elif Ação == "U":
            while True:
                while True:
                    grid, tabelas = BancoDeDados.Tables()
                    print(grid)
                    NomeTabela = input("Digite o número da tabela que deseja alterar: ")
                    while numeros(NomeTabela) == False:
                        NomeTabela = input("Digite um número de tabela corretamente!\n")
                    NomeTabela = int(NomeTabela)
                    NomeTabela = VerificarTabela(NomeTabela, tabelas)
                    while NomeTabela == -1:
                        NomeTabela = input("Digite um número de tabela existente!\n")
                        while numeros(NomeTabela) == False:
                            NomeTabela = input("Digite um número de tabela corretamente!\n")
                        NomeTabela = int(NomeTabela)
                        NomeTabela = VerificarTabela(NomeTabela, tabelas)

                    Id = input("Digite o Id do registro que deseja alterar: ")
                    while Id.isnumeric() == False or int(Id) <= 0:
                        Id = input("Digite um número válido: ")
                    Id = int(Id)
                    teste = BancoDeDados.UpdateTable(NomeTabela, Id)
                    if teste == 0:
                        resp = input(f"Ouve um erro ao tentar alterar o registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                        if resp == "n":
                            break
                        else:
                            continue
                    elif teste == 2:
                        resp = input(f"Esse registro não foi encontrado na tabela {NomeTabela}, deseja inserir um registro?(s/n)\n")
                        resp = BancoDeDados.ValidarResposta(resp)
                        if resp == "s":
                            while True:
                                teste = BancoDeDados.InsertTable(NomeTabela)
                                if teste == 0:
                                    resp = input(f"Ouve um erro ao tentar inserir 1 registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                                    resp = BancoDeDados.ValidarResposta(resp)
                                    if resp == "n":
                                        break
                                    else:
                                        continue
                                else:
                                    resp = input("Deseja fazer outra inserção?(s/n)\n")
                                    resp = BancoDeDados.ValidarResposta(resp)
                                    if resp == "n":
                                        break
                                    else:
                                        continue
                            break
                    else:
                        break
                resp = input("Deseja fazer outra alteração?(s/n)\n")
                resp = BancoDeDados.ValidarResposta(resp)
                if resp == "n":
                    break

        else:
            while True:
                while True:
                    grid, tabelas = BancoDeDados.Tables()
                    print(grid)
                    NomeTabela = input("Digite o número da tabela que deseja realizar o delete: ")
                    while numeros(NomeTabela) == False:
                        NomeTabela = input("Digite um número de tabela corretamente!\n")
                    NomeTabela = int(NomeTabela)
                    NomeTabela = VerificarTabela(NomeTabela, tabelas)
                    while NomeTabela == -1:
                        NomeTabela = input("Digite um número de tabela existente!\n")
                        while numeros(NomeTabela) == False:
                            NomeTabela = input("Digite um número de tabela corretamente!\n")
                        NomeTabela = int(NomeTabela)
                        NomeTabela = VerificarTabela(NomeTabela, tabelas)

                    Id = input("Digite o Id do registro que será excluído: ")
                    while Id.isnumeric() == False or int(Id) <= 0:
                        Id = input("Digite um número válido: ")
                    teste = BancoDeDados.Delete(NomeTabela, Id)
                    if teste == 0:
                        resp = input(
                            f"Ouve um erro ao tentar excluir o registro da tabela {NomeTabela}, deseja tentar novamente?(s/n)\n")
                        resp = BancoDeDados.ValidarResposta(resp)
                        if resp == "n":
                            break
                        else:
                            continue
                    else:
                        break
                resp = input("Deseja fazer outra exclusão? (s/n)\n")
                resp = BancoDeDados.ValidarResposta(resp)
                if resp == "n":
                    break

        resp = input("Deseja retornar ao menu?(s/n)\n")
        resp = BancoDeDados.ValidarResposta(resp)
        if resp == "n":
            break



print("-"*50)
print(f'{"Fim da execução do programa":^50}')
print("-"*50)