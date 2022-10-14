from reportlab.pdfgen import canvas
from prettytable import PrettyTable
import mysql.connector

def AcharProfessor(idProfessor):
    try:
        num = idProfessores.index(idProfessor)
        return True
    except:
        return False

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
            return tabela
        else:
            query.close()
            return 2
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        return 0

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

def regua(pdf):
    '''
    :param pdf: Parâmetro que recebe o objeto pdf
    :return: rotina que imprimi os números de linhas e colunas da página pdf
    '''
    pdf.setFillColor("red")
    for coluna in range(0,595):
        pdf.setFont("Helvetica-Oblique", 2)
        pdf.drawString(coluna, 0, f"{coluna}")
    for linha in range(0, 841, 5):
        pdf.setFont("Helvetica-Oblique", 2)
        pdf.drawString(0, linha, f"{linha}")


OpenDatabase("univap_db")


while True:
    print("-" * 20)
    print(f"{'MENU':^20}")
    print("-" * 20)
    print("• Deseja consultar dados completos de um professor? | 1")
    print("• Deseja consultar os dados completos de professores cujo nomes iniciem com um caractere específico? | 2")
    print("• Deseja consultar os nomes de todas as disciplinas de um curso? | 3")
    print("• Deseja consultar os nomes de todos os professores de um curso? | 4")
    print("• Deseja consultar a carga horária Total de um curso de um ano letivo específico? | 5")
    print("-" * 20)
    resp = input("Escolha uma opção para gerar um PDF: ")

    while resp.isnumeric() == False or int(resp) < 1 or int(resp) > 5:
        resp = input("Digite uma das alternativas a cima!\n")


    if resp == "1":
        idProfessores = []
        Professores = SelectALl("professores_tb")

        for professor in Professores:
            idProfessores.append(professor[0])
        print(idProfessores)
        idProfessor = input("Digite o número de registro de um professor: ")
        while idProfessor.isnumeric() == False or int(idProfessor) < 0 or AcharProfessor(int(idProfessor)) == False:
            idProfessor = input("Digite um registro válido!\n")
        idProfessor = int(idProfessor)
        Professor = Select("professores_tb", idProfessor)
        print(f"ID: {Professor[0][0]} | {Professor[0][1]}")
        print(f"Telefone: {Professor[0][2]}\nIdade: {Professor[0][3]}\nSalario: {Professor[0][4]}")
        try:
            nomeArquivo = input("Digite o nome do arquivo: ")
            while nomeArquivo == "":
                nomeArquivo = input("Digite um nome válido!\n")
            pdf = canvas.Canvas(f"{nomeArquivo}.pdf")
            regua(pdf)
            pdf.setFillColor("black")
            pdf.setTitle("Relatório de um Professor")
            pdf.setFont("Helvetica-Oblique", 16)
            pdf.drawString(10, 750, f'Dados Completos do Professor {Professor[0][1]}: ')
            pdf.setFont("Helvetica-Oblique", 14)
            pdf.drawString(10,720, f"ID: {Professor[0][0]} | {Professor[0][1]}")
            pdf.drawString(10, 700, f"Telefone: {Professor[0][2]}")
            pdf.drawString(10, 680, f"Idade: {Professor[0][3]}")
            pdf.drawString(10, 660, f"Salario: {Professor[0][4]}")
            pdf.save()
            print(f"{nomeArquivo} foi gerado com sucesso!")
        except Exception as erro:
            print(f"Erro ao gerar o pdf: {erro}")



    elif resp == "2":
        letra = input("Digite a letra que deseja consultar: ")
        while len(letra) > 1:
            letra = input("Digite apenas uma letra!\n")
        query = conexão.cursor()
        query.execute(f"select * from professores_tb where locate('{letra}', left(nomeProf, 1));")
        Professor = query.fetchall()
        if len(Professor) > 0 :
            print(f"ID: {Professor[0][0]} | {Professor[0][1]}")
            print(f"Telefone: {Professor[0][2]}\nIdade: {Professor[0][3]}\nSalario: {Professor[0][4]}")
            try:
                nomeArquivo = input("Digite o nome do arquivo: ")
                while nomeArquivo == "":
                    nomeArquivo = input("Digite um nome válido!\n")
                pdf = canvas.Canvas(f"{nomeArquivo}.pdf")
                regua(pdf)
                pdf.setFillColor("black")
                pdf.setTitle("Relatório de um Professor")
                pdf.setFont("Helvetica-Oblique", 16)
                pdf.drawString(10, 750, f'Dados Completos do Professor {Professor[0][1]}: ')
                pdf.setFont("Helvetica-Oblique", 14)
                pdf.drawString(10,720, f"ID: {Professor[0][0]} | {Professor[0][1]}")
                pdf.drawString(10, 700, f"Telefone: {Professor[0][2]}")
                pdf.drawString(10, 680, f"Idade: {Professor[0][3]}")
                pdf.drawString(10, 660, f"Salario: {Professor[0][4]}")
                pdf.save()
                print(f"{nomeArquivo} foi gerado com sucesso!")
            except Exception as erro:
                print(f"Erro ao gerar o pdf: {erro}")
        else:
            print(f"Não foi encontrado nenhum professor com a inicial {letra}")
    elif resp == "3":

        query = conexão.cursor()
        query.execute("select distinct curso from disciplinasxprofessores_tb;")
        Cursos = query.fetchall()
        cursos = []
        print("-"*10)
        for curso in Cursos:
            cursos.append(curso[0])
            print(f"Curso: {curso[0]}")
        print("-" * 10)
        curso = input("Digite o curso que deseja consultar: ")
        while True:
            try:
                num = cursos.index(int(curso))
                break
            except:
                curso = input("Digite um curso exitente!\n")

        query.execute(f"select codigoDisc, nomeDisc from disciplinas_tb d join disciplinasxprofessores_tb dp on d.codigoDisc = dp.codigoDisciplina where curso = {curso}")
        Disciplinas = query.fetchall()
        for i in range(len(Disciplinas)):
            print(f"ID: {Disciplinas[i][0]} | Disciplina: {Disciplinas[i][1]}")
        try:
            nomeArquivo = input("Digite o nome do arquivo: ")
            while nomeArquivo == "":
                nomeArquivo = input("Digite um nome válido!\n")
            pdf = canvas.Canvas(f"{nomeArquivo}.pdf")
            regua(pdf)
            pdf.setFillColor("black")
            pdf.setTitle("Relatório de Disciplinas")
            pdf.setFont("Helvetica-Oblique", 16)
            pdf.drawString(10, 750, f'Todas as disciplinas do curso {curso}: ')
            pdf.setFont("Helvetica-Oblique", 14)
            x = 720
            for i in range(len(Disciplinas)):
                pdf.drawString(10, x, f"ID: {Disciplinas[i][0]} | Disciplina: {Disciplinas[i][1]}")
                x-= 20
            pdf.save()
            print(f"{nomeArquivo} foi gerado com sucesso!")
        except Exception as erro:
            print(f"Erro ao gerar o pdf: {erro}")

    elif resp == "4":
        query = conexão.cursor()
        query.execute("select distinct curso from disciplinasxprofessores_tb;")
        Cursos = query.fetchall()
        cursos = []
        print("-" * 10)
        for curso in Cursos:
            cursos.append(curso[0])
            print(f"Curso: {curso[0]}")
        print("-" * 10)
        curso = input("Digite o curso que deseja consultar: ")
        while True:
            try:
                num = cursos.index(int(curso))
                break
            except:
                curso = input("Digite um curso exitente!\n")
        query.execute(f"select distinct registro, nomeProf from professores_tb p join disciplinasxprofessores_tb dp on p.registro = dp.codigoProfessor where curso = {curso};")
        Professores = query.fetchall()
        for i in range(len(Professores)):
            print(f"ID: {Professores[i][0]} | Professor: {Professores[i][1]}")
        try:
            nomeArquivo = input("Digite o nome do arquivo: ")
            while nomeArquivo == "":
                nomeArquivo = input("Digite um nome válido!\n")
            pdf = canvas.Canvas(f"{nomeArquivo}.pdf")
            regua(pdf)
            pdf.setFillColor("black")
            pdf.setTitle("Relatório de Professores")
            pdf.setFont("Helvetica-Oblique", 16)
            pdf.drawString(10, 750, f'Todas os professores do curso {curso}: ')
            pdf.setFont("Helvetica-Oblique", 14)
            x = 720
            for i in range(len(Professores)):
                pdf.drawString(10, x, f"ID: {Professores[i][0]} | Professor: {Professores[i][1]}")
                x-= 20
            pdf.save()
            print(f"{nomeArquivo} foi gerado com sucesso!")
        except Exception as erro:
            print(f"Erro ao gerar o pdf: {erro}")

    elif resp == "5":
        query = conexão.cursor()
        query.execute("select distinct anoLetivo from disciplinasxprofessores_tb;")
        Anos = query.fetchall()
        anos = []
        print("-" * 10)
        for ano in Anos:
            anos.append(ano[0])
            print(f"Ano Letivo: {ano[0]}")
        print("-" * 10)
        ano = input("Digite o ano letivo que deseja consultar: ")
        while True:
            try:
                num = anos.index(int(ano))
                break
            except:
                ano = input("Digite um curso exitente!\n")
        query.execute(f"select sum(cargaHoraria) as `Carga Horaria Total` from disciplinasxprofessores_tb where anoLetivo = {ano}")
        CargaHoraria = query.fetchall()
        print(f"Carga horária total do ano letivo {ano}: {CargaHoraria[0][0]}")

        try:
            nomeArquivo = input("Digite o nome do arquivo: ")
            while nomeArquivo == "":
                nomeArquivo = input("Digite um nome válido!\n")
            pdf = canvas.Canvas(f"{nomeArquivo}.pdf")
            regua(pdf)
            pdf.setFillColor("black")
            pdf.setTitle("Relatório de Carga Horária")
            pdf.setFont("Helvetica-Oblique", 16)
            pdf.drawString(10, 750, f'Carga Horaria total do ano letivo {ano}: ')
            pdf.setFont("Helvetica-Oblique", 14)
            pdf.drawString(10, 720, f"Carga Horária total: {CargaHoraria[0][0]} horas")
            pdf.save()
            print(f"{nomeArquivo} foi gerado com sucesso!")
        except Exception as erro:
            print(f"Erro ao gerar o pdf: {erro}")

    resp = input("Deseja gerar outro pdf? (s/n): ")
    while resp != "s" and resp != "n":
        resp = input("Digite umaresposta válida!\n")
    if resp == "n":
        break