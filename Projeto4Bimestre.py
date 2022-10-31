import mysql.connector
import pandas as pd
from prettytable import PrettyTable
from colorama import Fore, Back

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
            print("Conexão não realizada")
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

def Professores2021():

    try:
        query = conexão.cursor()
        grid = PrettyTable(["Registro", "Nome do Professor"])
        query.execute("select DISTINCT registro, nomeProf  from professores p join disciplinasxprofessores d on p.registro = d.codProfessor where d.anoLetivo = 2021")
        tabela = query.fetchall()
        if query.rowcount > 0:
            professores = []
            for i in range(len(tabela)):
                grid.add_row(tabela[i])
                professores.append(tabela[i][0])
                professores.append(tabela[i][1])
            print(grid)
            query.close()
            return professores
        else:
            print(f"Não há registro na tabela professores")
            query.close()
            return 2
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0

def DadosDisciplinasxProfessores(id):
    try:
        query = conexão.cursor()
        query.execute(f"select * from disciplinasxprofessores where codprofessor = {id}")
        tabela = query.fetchall()
        dicionario = {}
        dicionario["Professor"] = id
        disciplinas = []
        cursos = []
        cargaHoraria = []
        anosletivos = []
        for registro in tabela:
            if registro[5] == 2021:
                disciplinas.append(registro[1])

                cursos.append(registro[3])
                cargaHoraria.append(registro[4])

                anosletivos.append(registro[5])
        dicionario["Disciplinas"] = disciplinas
        dicionario["Cursos"] = cursos
        dicionario["Cargas Horárias"] = cargaHoraria
        dicionario["Anos Letivos"] = anosletivos
        return dicionario
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")



def Disciplinas(id):
    try:
        query = conexão.cursor()
        query.execute(f"select nomedisc from disciplinas where codigodisc = {id}")
        nomeDisciplinas = query.fetchall()
        query.close()
        return nomeDisciplinas[0][0]
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")



def RelaçãoProfessoresNoCurso():
    try:
        query = conexão.cursor()
        query.execute("select distinct curso, codprofessor, p.nomeprof from disciplinasxprofessores d join professores p on p.registro = d.codprofessor order by curso, nomeprof")
        tabela = query.fetchall()
        dicionario = {}
        cursos = []
        professores = []
        qtdProfs = []
        for registro in tabela:
            cursos.append(registro[0])
            professores.append(registro[2])
        dicionario["Cursos"] = cursos
        dicionario["Professores"] = professores
        teste = []
        for curso in cursos:
            if curso not in teste:
                teste.append(curso)
        for i in range(len(cursos)):
            for x in range(len(teste)):
                if teste[x] == cursos[i]:
                    qtdProfs.append(cursos.count(teste[x]))
        dicionario["Qtd Professores"] = qtdProfs

        df = pd.DataFrame(dicionario)
        return df
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")


def RelaçãoDisciplinasNoCurso():
    try:
        query = conexão.cursor()
        query.execute(f"select curso, di.nomedisc, cargahoraria from disciplinasxprofessores d join disciplinas di on d.coddisciplina = di.codigodisc")
        tabela = query.fetchall()
        dicionario = {}
        cursos = []
        disciplinas = []
        cargaHorariaTotal = []
        for registro in tabela:
            cursos.append(registro[0])
            disciplinas.append(registro[1])
        dicionario["Cursos"] = cursos
        dicionario["Disciplinas"] = disciplinas
        teste = []
        for curso in cursos:
            if curso not in teste:
                teste.append(curso)

        for x in range(len(teste)):
            horas = 0
            for i in range(len(tabela)):
                if teste[x] == tabela[i][0]:
                    horas += tabela[i][2]
            for i in range(len(tabela)):
                if teste[x] == tabela[i][0]:
                    cargaHorariaTotal.append(horas)
        dicionario["Carga Horária Total"] = cargaHorariaTotal
        df = pd.DataFrame(dicionario)
        return df

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")


print(Back.BLACK + Fore.LIGHTWHITE_EX + "-"*50)
print(Fore.GREEN + f'{"Gerador de Excel":^50}' + Fore.RESET)
print(Fore.CYAN + "desenvolvido por: Miguel Brito - Lucas Maia - Raul Fernandes" + Fore.RESET)
print(Back.BLACK + Fore.LIGHTWHITE_EX +  "-"*50)

OpenDatabase("univap")

while True:
    professores = Professores2021()
    idProf = input("Digite o registro do professor que deseja salvar os dados em excel: ")
    while not idProf.isnumeric() or professores.count(int(idProf)) == 0:
        idProf = input("Digite um registro existente!\n")
    idProf = int(idProf)
    for i in range(len(professores)):
        if idProf == professores[i]:
            nomeProf = professores[i+1]
    dicionarioProf = DadosDisciplinasxProfessores(idProf)
    disciplinas = []
    for disciplina in dicionarioProf["Disciplinas"]:
        disciplinas.append(Disciplinas(disciplina))
    dicionarioProf["Disciplinas"] = disciplinas
    dicionarioProf["Professor"] = nomeProf
    df1 = pd.DataFrame(dicionarioProf)
    df1["Total de Horas Aulas"] = sum(df1["Cargas Horárias"])
    df2 = RelaçãoProfessoresNoCurso()
    df3 = RelaçãoDisciplinasNoCurso()

    excel = pd.ExcelWriter("Projeto4Bimestre.xlsx", engine="openpyxl")
    df1.to_excel(excel, sheet_name="a", index=False)
    df2.to_excel(excel, sheet_name="b", index=False)
    df3.to_excel(excel, sheet_name="c", index=False)

    excel.save()

    resp = input("Deseja gerar outro arquivo excel? (s/n)")
    while resp != "s" and resp != "n":
        resp = input("Digite uma resposta válida!")
    if resp == "n":
        break