import mysql.connector
from prettytable import PrettyTable


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
    query.close()
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
            return tabela
        else:
            print(f"Não a registro na tabela {NomeTabela}")
            query.close()
            return 2
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0

OpenDatabase("univap_db")

Professores = SelectALl("Professores_tb")

for i in range(len(Professores)):
    query = conexão.cursor()
    NomeColunas = Columns("disciplinasxprofessores_tb")
    grid = PrettyTable(NomeColunas)
    query.execute(f"select * from disciplinasxprofessores_tb where codigoProfessor = {Professores[i][0]};")
    Arquivo = open(f"{Professores[i][0]}.html", "w")
    disciplinaProfessor = query.fetchall()
    texto = f"Disciplinas do professor: {Professores[i][1]}<br>"
    for x in range(len(disciplinaProfessor)):
        query.execute(f"select * from disciplinas_tb where codigoDisc = {disciplinaProfessor[x][1]}")
        Disciplinas = query.fetchall()

        if x != 0 and disciplinaProfessor[x][3] != disciplinaProfessor[x-1][3]:
            texto += f"<br>Curso: {disciplinaProfessor[x][3]}<br>"
        if x == 0:
            texto += f"Curso: {disciplinaProfessor[x][3]}<br>"
            texto += "CÓDIGO DA DISCIPLINA | NOME DA DISCIPLINA<br>"
        for y in range(len(Disciplinas)):
            texto += f"{Disciplinas[0][0]} | {Disciplinas[0][1]}<br>"
    Arquivo.write(texto)
