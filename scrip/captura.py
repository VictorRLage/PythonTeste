import subprocess
import mysql.connector
import psutil
import numpy
import datetime
import functools
import operator



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

def Conexao(user, senha, host, database):
        global cnx
        cnx = mysql.connector.connect(user=user, password=senha, host=host, database=database, raise_on_warnings=True)

        if cnx.is_connected():
            db_info = cnx.get_server_info()
            print('conectado', db_info)
            global cursor
            cursor = cnx.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados:", linha)



def teste():
        print("Inserindo leitura no banco...")
        datahora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(datahora)
        exec(strNome + " = " + strCodigo, globals())
        var_leitura = globals()[strNome]
        tuple_leitura = (var_leitura,)
        print(tuple_leitura)
        print(type(tuple_leitura))        

        sql = ("INSERT INTO Leitura (Leitura, DataHora, fkTorre, fkComponente) VALUES (%s, %s, %s, %s)")
        values = (var_leitura, datahora, idTorre , y)


        try:
            # Executando comando SQL   
            cursor.execute(sql, values)

            # Commit de mudanças no banco de dados
            cnx.commit()

            print("Leitura inserida no banco")

        except mysql.connector.Error as err:
            cnx.rollback()
            print("Something went wrong: {}".format(err))

            

def InserindoLeitura():
    # PREGAR fkCOMPONENTE
            queryComponente = ("SELECT `fkComponente` FROM Torre_Componente " 
                    "WHERE Torre_Componente.fkTorre = %s;")

            try:
                # Executing the SQL command
                cursor.execute(queryComponente, (idTorre))
                print("Pegando os componentes da torre...")

            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

            fkComponente= cursor.fetchall()
            vet_fkComponente = numpy.asarray(fkComponente)
            print("Componentes da maquina:", vet_fkComponente)

            
            for x in vet_fkComponente:
                print(x)
                global y
                y = int(x[0])
                print(y)

                # PEGAR CODIGO COMPONENTE
                queryCodigo = ("SELECT `Codigo` FROM Componente " 
                    "WHERE Componente.idComponente = %s;")

                try:
                    # Executing the SQL command
                    cursor.execute(queryCodigo, (y,))
                    print("Pegando codigo do componente ", y,'...')

                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))

                Codigo = cursor.fetchone()
                print("Codigo do componente ",y,":", Codigo)

                def convertTuple(tup):
                    str = functools.reduce(operator.add, (tup))
                    return str

                global strCodigo
                strCodigo = convertTuple(Codigo)            


                # PREGAR NOME COMPONENTE
                queryNome = ("SELECT `Nome` FROM Componente " 
                    "WHERE Componente.idComponente = %s;")

                try:
                    # Executing the SQL command
                    cursor.execute(queryNome, (y,))
                    print("Pegando nome do componente", y)

                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))

                Nome= cursor.fetchone()
                global strNome
                strNome = convertTuple(Nome)
                print("Nome componente ",y,":", strNome)
                print(strNome + " = " + strCodigo)
                teste()

def VerificarDadosMaquina(SerialID):


    query = ("SELECT `idTorre` FROM Torre "
                    "WHERE SerialID = %s;")
    print(SerialID)             
    try:
        # Executando comando SQL
        cursor.execute(query, (SerialID,))
        print("Encontrou a torre")
        global idTorre
        idTorre = cursor.fetchone()


    except mysql.connector.Error as err:
        print("Não encontrou a torre")
        print("Something went wrong: {}".format(err))


    query = ("SELECT `SerialID` FROM Torre "
                    "WHERE idTorre = %s;")
                    
    try:
        # Executando comando SQL
        cursor.execute(query, (idTorre))
        print("Verificando dados da torre...")
        SerialID = cursor.fetchone()


    except mysql.connector.Error as err:
        print("Não encontrou a torre")
        print("Something went wrong: {}".format(err))
    
    if SerialID is not None:
        print("A torre possui dados cadastrados")
        print("Cadastrando leituras...")
        InserindoLeitura()
    else:
        print("A torre não possui dados")
        InserirDadosMaquina(strip_SerialIdAtual, strip3_OsAtual, strip3_MaquinaAtual, strip2_ProcessadorAtual, strip2_DiscoAtual, strip2_RamAtual)


        

    


def InserirDadosMaquina(SerialID, OS, Maquina, Processador, Disco, RamSpeed):

    sql = ("UPDATE Torre  SET SerialID = %s,  SO = %s, Maquina = %s, Processador = %s, Disco = %s, VelocidadeRam = %s,  fkEmpresa = %s WHERE idTorre = 101")
    values = (SerialID, OS, Maquina, Processador, Disco, RamSpeed, 1)

    try:
    # Executando comando SQL
        cursor.execute(sql, values)

        # Commit de mudanças no banco de dados
        cnx.commit()

        print("Inserindo dados...")

    except mysql.connector.Error as err:
        cnx.rollback()
        print("Something went wrong: {}".format(err))



Conexao('tecnico','urubu100','localhost','Monitoll')
VerificarDadosMaquina(strip_SerialIdAtual)