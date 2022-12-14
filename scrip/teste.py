from statistics import mean
import subprocess
import time
import psutil
import numpy
import datetime
import functools
import operator
import pyodbc
import textwrap



def Login():
    u_email = input('Seu e-mail: ')
    u_senha = input('Sua senha: ')
    ValidacaoLogin(u_email,u_senha)
    


def ValidacaoLogin(u_email,u_senha):

    selectnome_sql = "SELECT Nome FROM Usuario WHERE Email = ? and Senha = ?;"
    records = (u_email, u_senha)
                    
    try:
        # Executando comando SQL
        cursor.executemany(selectnome_sql, records)
        print("Fazendo login...")
        usuario = cursor.fetchone()
        

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
    
    if usuario is not None:
        def convertTuple(tup):
            str = ''
            for item in tup:
                str = str + item
            return str
        str_usuario = convertTuple(usuario)
        print('Olá,',str_usuario,'!')

        selecfkempresa_sql = "SELECT fkEmpresa FROM Usuario WHERE Email = ? and Senha = ?;"
        records2 = (u_email, u_senha)
                    
        try:
            # Executando comando SQL
            cursor.execute(selecfkempresa_sql, records2)
            global fkEmpresa
            fkEmpresa = cursor.fetchone()
            global int_fkEmpresa
            int_fkEmpresa = sum(fkEmpresa)
            print('fkEmpresa:', fkEmpresa)
        

        except pyodbc.Error as err:
            print("Something went wrong: {}".format(err))

        SelectIdTorres(fkEmpresa)


    else:
        print('Email ou senha incoretos')
        Login()

def EscolherTorres(idTorres):
    maquinas = numpy.asarray(idTorres)
    print('Maquinas:', maquinas)
    global idTorre
    idTorre = input('Qual é esta maquina?')

def SelectIdTorres(fkEmpresa):

    selectfkempresa2_sql = "SELECT idTorre FROM Torre WHERE fkEmpresa = ?;"                    
    try:
        # Executando comando SQL
        cursor.execute(selectfkempresa2_sql, (fkEmpresa))
        idTorres = cursor.fetchall()
        print(idTorres)
        

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
    
    EscolherTorres(idTorres)


# Bloco pegar serial id
byte_SerialIdAtual = subprocess.check_output('''sudo dmidecode -s system-serial-number''', shell=True)
str_SerialIdAtual = byte_SerialIdAtual.decode('UTF-8')
global strip_SerialIdAtual
strip_SerialIdAtual = str_SerialIdAtual.strip('\n')

# Bloco pegar sistema operacional
byte_OsAtual = subprocess.check_output('''lsb_release -d''', shell=True)
str_OsAtual = byte_OsAtual.decode('UTF-8')
strip_OsAtual = str_OsAtual.strip('Description:')
strip2_OsAtual = strip_OsAtual.strip('\t')
global strip3_OsAtual
strip3_OsAtual = strip2_OsAtual.strip('\n')

# Bloco pegar modelo maquina
byte_MaquinaAtual = subprocess.check_output('''sudo dmidecode -t 1 | grep 'Product Name' | uniq''', shell=True)
str_MaquinaAtual = byte_MaquinaAtual.decode('UTF-8')
strip_MaquinaAtual = str_MaquinaAtual.strip('\tProduct')
strip2_MaquinaAtual = strip_MaquinaAtual.strip(' Name: ')
global strip3_MaquinaAtual
strip3_MaquinaAtual = strip2_MaquinaAtual.strip('\n')

# Bloco pegar processador
byte_ProcessadorAtual = subprocess.check_output('''lscpu | grep 'Model name:' | uniq''', shell=True)
str_ProcessadorAtual = byte_ProcessadorAtual.decode('UTF-8')
strip_ProcessadorAtual = str_ProcessadorAtual.strip('Model name:')
global strip2_ProcessadorAtual
strip2_ProcessadorAtual = strip_ProcessadorAtual.strip('\n')

# Bloco pegar disco 
byte_DiscoAtual = subprocess.check_output('''sudo lshw -class disk -class storage | grep -B1 'vendor' | head -1''', shell=True)
str_DiscoAtual = byte_DiscoAtual.decode('UTF-8')
strip_DiscoAtual = str_DiscoAtual.strip('\tproduct: ')
global strip2_DiscoAtual
strip2_DiscoAtual = strip_DiscoAtual.strip('\n')

# Bloco pegar velocidade da ram
byte_RamAtual = subprocess.check_output('''sudo dmidecode --type memory | grep -B1 'Type Detail: ' | head -1''', shell=True)
str_RamAtual = byte_RamAtual.decode('UTF-8')
strip_RamAtual = str_RamAtual.strip('\tType: ')
global strip2_RamAtual
strip2_RamAtual = strip_RamAtual.strip('\n')

def Conexao():
        global cnx
        #Definindo o driver
        driver = '{ODBC Driver 18 for SQL Server}'
        # definindo server e database
        server_name = 'montioll'
        database_name = 'Monitoll'
        server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
        # definindo o nome e a senha 
        username = 'Monitoll'
        password = 'Grupo7@123'
        # definindo o banco url
        cnx = connection_string = textwrap.dedent("""
            Driver={driver};
            Server={server};
            Database={database};
            Uid={username};
            Pwd={password};
            Encrypt=yes;
            TrustedServerCertificate=no;
            Connection Timeout=10;
        """.format(
            driver=driver,
            server=server,
            database=database_name,
            username=username,
            password=password
        ))
        global cursor
        cursor = cnx.cursor()
        
        # criando o objeto de conecxao
        cnxn:pyodbc.Connection = pyodbc.connect(connection_string)    


def teste():
        print("Inserindo leitura no banco...")
        datahora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(datahora)
        exec(strNome + " = " + strCodigo, globals())
        var_leitura = globals()[strNome]
        if strNome == 'porcentagem_por_nucleo':
            print('caiu no if')
            soma = 0
            for x in var_leitura:
                soma = soma + x
                PorcentCPU = (round(soma/processadores_qtd, 1))
            print(PorcentCPU)
            var_leitura2 = PorcentCPU
        elif strNome == 'pacotes_perdidos_porcentagem':
            print('caiu no elif 1')
            var_leitura2 = round((((pacotes_perdidos_porcentagem[1] - pacotes_perdidos_porcentagem[0])/pacotes_perdidos_porcentagem[1])*100), 1)
        elif strNome == 'processadores_nucleo_porcentagem':
            print('caiu no elif 2')
            var_leitura2 = numpy.mean(var_leitura) 
        else:
            print('caiu no else')
            var_leitura2 = var_leitura
        print(var_leitura2)

        insert_sql = "INSERT INTO Leitura (Leitura, DataHora, fkTorre, fkComponente) VALUES (?, ?, ?, ?)"
        records = (var_leitura2, datahora, idTorre , y)

        try:
        # Executando comando SQL   
            crsr.executemany(insert_sql, records)

            # Commit de mudanças no banco de dados
            cnx.commit()

            print("Leitura inserida no banco")
        except pyodbc.Error as err:
            cnx.rollback()
            print("Something went wrong: {}".format(err))
            

def InserindoLeitura():
    # PREGAR fkCOMPONENTE
            selectcomponente_sql = "SELECT fkComponente FROM Torre_Componente WHERE Torre_Componente.fkTorre = %s;"

            try:
                # Executing the SQL command
                cursor.execute(selectcomponente_sql, (idTorre,))
                print("Pegando os componentes da torre...")

            except pyodbc.Error as err:
                print("Something went wrong: {}".format(err))
                print('teste exept')

            fkComponente= cursor.fetchall()
            print(fkComponente)
            vet_fkComponente = numpy.asarray(fkComponente)
            print("Componentes da maquina:", vet_fkComponente)

            
            for x in vet_fkComponente:
                print(x)
                global y
                y = int(x[0])
                print(y)

                # PEGAR CODIGO COMPONENTE
                selectCodigo_sql = "SELECT Codigo FROM Componente WHERE Componente.idComponente = %s;"

                try:
                    # Executing the SQL command
                    cursor.execute(selectCodigo_sql, (y,))
                    print("Pegando codigo do componente ", y,'...')

                except pyodbc.Error as err:
                    print("Something went wrong: {}".format(err))

                Codigo = cursor.fetchone()
                print("Codigo do componente ",y,":", Codigo)

                def convertTuple(tup):
                    str = functools.reduce(operator.add, (tup))
                    return str

                global strCodigo
                strCodigo = convertTuple(Codigo)            


                # PREGAR NOME COMPONENTE
                selectNomeC_sql = "SELECT Nome FROM Componente WHERE Componente.idComponente = %s;"

                try:
                    # Executing the SQL command
                    cursor.execute(selectNomeC_sql, (y,))
                    print("Pegando nome do componente", y)

                except pyodbc.Error as err:
                    print("Something went wrong: {}".format(err))

                Nome= cursor.fetchone()
                global strNome
                strNome = convertTuple(Nome)
                print("Nome componente ",y,":", strNome)
                print(strNome + " = " + strCodigo)
                teste()

def VerificarDadosMaquina(idTorre):


    selectidtorre_sql = "SELECT SerialID FROM Torre WHERE idTorre = %s;"
                    
    try:
        # Executando comando SQL
        cursor.execute(selectidtorre_sql, (idTorre,))
        print("Verificando dados da torre...")
        SerialIdBanco = cursor.fetchone()

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
    
    if SerialIdBanco[0] is not None:
        print("A torre possui dados cadastrados")
        print("Cadastrando leituras...")
        InserindoLeitura()
    else:
        print("A torre não possui dados")
        InserirDadosMaquina(strip_SerialIdAtual, strip3_OsAtual, strip3_MaquinaAtual, strip2_ProcessadorAtual, strip2_DiscoAtual, strip2_RamAtual)


        

    


def InserirDadosMaquina(SerialID, OS, Maquina, Processador, Disco, RamSpeed):

    update_sql = "UPDATE Torre  SET SerialID = %s,  SO = %s, Maquina = %s, Processador = %s, Disco = %s, VelocidadeRam = %s,  fkEmpresa = %s WHERE idTorre = %s"
    values = (SerialID, OS, Maquina, Processador, Disco, RamSpeed, int_fkEmpresa, idTorre)

    try:
    # Executando comando SQL
        cursor.execute(update_sql, values)

        # Commit de mudanças no banco de dados
        cnx.commit()

        print("Inserindo dados...")

    except pyodbc.Error as err:
        cnx.rollback()
        print("Something went wrong: {}".format(err))


Login()
while True:
    VerificarDadosMaquina(idTorre)
    time.sleep(10)
