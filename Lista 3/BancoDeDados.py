# Necessário: 'pip install mysql.connector.python', 'pip install prettytable' e 'pip install coloroma'


'''
Módulo para cadastrar, alterar, excluir e inserir em qualquer banco de dados relacional
que tenha tabelas com chaves primárias simples, e sejam o primeiro campo da tabela.
Suas funções são todas documentadas e pensadas para serem usadas de forma simples, com apenas alguns parâmetros.
O módulo também apresenta funções visuais como Prettytabel e o colorama, funções para facilitar a visualização dos
resultados obtidos pelas rotinas.
'''
from prettytable import PrettyTable
import mysql.connector
from colorama import Fore, Back, Style


print(Back.BLACK + Fore.LIGHTWHITE_EX + "-"*50)
print(Fore.GREEN + f'{"SITEMA DE BANCO DE DADOS":^50}' + Fore.RESET)
print(Fore.CYAN + "desenvolvido por: Miguel Brito" + Fore.RESET)
print(Back.BLACK + Fore.LIGHTWHITE_EX +  "-"*50)


def OpenDatabase(BancoDeDados):
    '''
    Essa rotina faz conexão com o banco de dados desejado.
    :param BancoDeDados: Como parâmetro essa rotina recebe o nome do banco de dados informado pelo usuário.
    :return: Retorna 1 para sucesso e 0 para falha.
    '''
    try:
        global conexão
        conexão = mysql.connector.Connect(host="localhost", database=BancoDeDados, user="root", password="")

        if conexão.is_connected():
            BancoInfo = conexão.get_server_info()
            print(f"Conexão feita com sucesso - Versão {BancoInfo}")

            global query
            query = conexão.cursor()
            query.execute("select database();")
            NomeBanco = query.fetchone()
            print("-"*50)
            print(f"{f'Banco de dados {NomeBanco[0]} acessado!':^50}")
            print("-"*50)
            query.close()
            return 1
        else:
            print("Conexão não realizada!")
            query.close()
            return 0

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0


def Tables():
    '''
    Essa rotina apresenta todas as tabelas criadas no banco de dados.
    :return: Retorna uma tabela com o nome de todas as tabelas do banco.
    '''
    grid = PrettyTable(["Tables_in_univap_db"])
    NomeTabelas = []
    try:
        query = conexão.cursor()
        query.execute("show tables;")
        tabela = query.fetchall()
        if query.rowcount > 0:
            for registro in tabela:
                grid.add_row(registro)
        return grid
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return "Erro"

def Columns(NomeTabela):
    '''
    Essa rotina retorna uma lista com o nome de todas as colunas de uma tabela digitada pelo usuário
    :param NomeTabela: Esse parâmetro é a tabela digitada pelo usuáiro
    :return NomeColunas: Lista com os nomes das colunas de uma tabela
    '''
    NomeColunas = []
    query = conexão.cursor()
    query.execute(f"select column_name from information_schema.columns where table_name = '{NomeTabela}';")
    colunas = query.fetchall()
    for x in colunas:
        NomeColunas.append(x[0])
    return NomeColunas


def SelectALl(NomeTabela):
    '''
    Essa rotina imprime todos os registros de uma tabela digitada pelo usuário.
    :param NomeTabela: Este parâmentro é a tabela que o usuário deseja consultar.
    :return: Retorna 1 para sucesso, 0 para falha e 2 caso a tabela não tenha registros.
    '''
    try:
        query = conexão.cursor()
        NomeColunas = Columns(NomeTabela)
        grid = PrettyTable(NomeColunas)
        query.execute(f"select * from {NomeTabela};")
        tabela = query.fetchall()
        if query.rowcount > 0:
            for i in range(len(tabela)):
                grid.add_row(tabela[i])
            print(grid)
            query.close()
            return 1
        else:
            print(f"Não a registro na tabela {NomeTabela}")
            return 2
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0


def InsertTable(NomeTabela):
    '''
    Essa rotina executa um registro em uma tabela digitada pelo usuário.
    :param NomeTabela: Tabela digitada pelo usuário.
    :return: Retorna 1 para sucesso e 0 para falha.
    '''
    try:
        query = conexão.cursor()
        NomeColunas = Columns(NomeTabela)
        valores = []
        for i in range(len(NomeColunas)):
            valores.append(input(f"Digite o {NomeColunas[i]}: "))
        values = ""
        for V in valores:
            if V.isnumeric():
                values += f"{V}, "
            else:
                values += f"'{V}', "
        values = values[:-2]

        campos = ""
        for colunas in NomeColunas:
            campos += f"{colunas}, "
        campos = campos[:-2]
        query.execute(f"insert into {NomeTabela}({campos}) values({values});")
        conexão.commit()
        print("Registro executado com sucesso!")
        return 1
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0


#FUNCIONA APENAS COM CHAVE PRIMARIA SIMPLES


def Select(NomeTabela, Id):
    '''
    Essa rotina imprime uma tabela com o registro designado pelo Id informado pelo usuário.
    :param NomeTabela: Tabela a ser consultada, digitada pelo usuário.
    :param Id: Id para que seja realizada a consulta, digitado pelo usuário.
    :return: Retorna 1 para sucesso e 0 para falha.
    '''
    try:
        NomeColunas = Columns(NomeTabela)
        grid = PrettyTable(NomeColunas)
        query = conexão.cursor()
        query.execute(f"select * from {NomeTabela} where {NomeColunas[0]} = {Id};")
        tabela = query.fetchall()
        if query.rowcount > 0:
            for i in range(len(tabela)):
                grid.add_row(tabela[i])
            print(grid)
            query.close()
            return 1

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0


def UpdateTable(NomeTabela, Id):
    '''
    Essa rotina faz uma alteração na tabela com o registro designado pelo Id informado pelo usuário.
    :param NomeTabela: Tabela que será alterada, digitada pelo usuário.
    :param Id: Id para que seja realizada a alteração, digitado pelo usuário.
    :return: Retorna 1 para sucesso e 0 para falha.
    '''
    try:
        query = conexão.cursor()
        NomeColunas = Columns(NomeTabela)
        if NomeTabela != "disciplinasxprofessores_tb":
            query.execute("select * from disciplinasxprofessores_tb")
            ChaveEstrangeira = query.fetchall()
            if ChaveEstrangeira[0][1] == int(Id):
                print(f"Chave estrangeira detectada!\nAntes de alterar a tabela {NomeTabela}, cheque as informações da tabela disciplinasxprofessores")
                return 0
            elif ChaveEstrangeira[0][2] == int(Id):
                print(f"Chave estrangeira detectada!\nAntes de alterar a tabela {NomeTabela}, cheque as informações da tabela disciplinasxprofessores")
                return 0
        valores = []
        for i in range(1, len(NomeColunas)):
            valores.append(input(f"Digite o {NomeColunas[i]}: "))

        campos = ""
        num = len(NomeColunas)
        if num > 2:
            for i in range(1, num -1):
                campos += f'{NomeColunas[i]}="'
                campos += f'{valores[i-1]}", '
            campos = campos[:-2]
        else:
            for i in range(1, num):
                campos += f'{NomeColunas[i]}="'
                campos += f'{valores[i-1]}", '
            campos = campos[:-2]
        query.execute(f"update {NomeTabela} set {campos} where {NomeColunas[0]} = {Id};")
        conexão.commit()
        print("Alteração executada com sucesso!")
        return 1
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0


def Delete(NomeTabela, Id):
    try:
        NomeColunas = Columns(NomeTabela)
        grid = PrettyTable(NomeColunas)
        query = conexão.cursor()
        if NomeTabela != "disciplinasxprofessores_tb":
            query.execute("select * from disciplinasxprofessores_tb")
            ChaveEstrangeira = query.fetchall()
            if ChaveEstrangeira[0][1] == int(Id):
                print(
                    f"Chave estrangeira detectada!\nAntes de alterar a tabela {NomeTabela}, cheque as informações da tabela disciplinasxprofessores")
                return 0
            elif ChaveEstrangeira[0][2] == int(Id):
                print(
                    f"Chave estrangeira detectada!\nAntes de alterar a tabela {NomeTabela}, cheque as informações da tabela disciplinasxprofessores")
                return 0
        query.execute(f"delete from {NomeTabela} where {NomeColunas[0]} = {int(Id)};")
        print("Exclusão realizada com sucesso!")
        query.close()
        return 1

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0
