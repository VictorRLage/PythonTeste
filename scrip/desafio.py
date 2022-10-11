import time
import subprocess
from tkinter import Y
from typing import Tuple
import psutil
import datetime
import mysql.connector
import functools
import operator
import numpy


i=0
# estrutura de repetição infinita
while True:
    
    # CAPTURA SERIALID CMD
    
    direct_output2 = subprocess.check_output(
        'wmic bios get serialnumber', shell=True)
    SerialID = direct_output2.decode('UTF-8')
    trim1SerialID = SerialID.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2SerialID = func(trim1SerialID)
    trim3SerialID = trim2SerialID.strip("SerialNumber") 
    trim4SerialID = trim3SerialID.strip()


    # CAPTURA OS CMD
    
    direct_output6 = subprocess.check_output(
        'wmic os get Caption', shell=True)
    OSnome = direct_output6.decode('UTF-8')
    trim1OSnome = OSnome.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2OSnome = func(trim1OSnome)
    trim3OSnome = trim2OSnome.strip("Caption") 
    trim4OSnome = trim3OSnome.strip()



    # CAPTURA MODELO MAQUINA CMD

    direct_output = subprocess.check_output(
        'wmic computersystem get model', shell=True)
    modeloPC = direct_output.decode('UTF-8')
    trim1ModeloPC = modeloPC.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2ModeloPC = func(trim1ModeloPC)
    trim3ModeloPC = trim2ModeloPC.strip("Model") 
    trim4ModeloPC = trim3ModeloPC.strip()



    # CAPTURA MODELO PROCESSADOR CMD
    
    direct_output3 = subprocess.check_output(
        'wmic cpu get name', shell=True)
    ModeloCPU = direct_output3.decode('UTF-8')
    trim1ModeloCPU = ModeloCPU.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2ModeloCPU = func(trim1ModeloCPU)
    trim3ModeloCPU = trim2ModeloCPU.strip("SerialNumber") 
    trim4ModeloCPU = trim3ModeloCPU.strip()



    # CAPTURA MODELO DISCO CMD
    
    direct_output4 = subprocess.check_output(
        'wmic diskdrive get model', shell=True)
    ModeloDR = direct_output4.decode('UTF-8')
    trim1ModeloDR = ModeloDR.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2ModeloDR = func(trim1ModeloDR)
    trim3ModeloDR = trim2ModeloDR.strip("Model") 
    trim4ModeloDR = trim3ModeloDR.strip()



    # CAPTURA RAM SPEED CMD
    
    direct_output5 = subprocess.check_output(
        'wmic memorychip get speed', shell=True)
    ramSpeed = direct_output5.decode('UTF-8')
    trim1ramSpeed = ramSpeed.strip()
    def func(value):
        return ''.join(value.splitlines())
    trim2ramSpeed = func(trim1ramSpeed)
    trim3ramSpeed = trim2ramSpeed.strip("Speed") 
    trim4ramSpeed = trim3ramSpeed.strip()









    def teste():
        datahora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(datahora)
        exec(strNome + " = " + strCodigo, globals())
        var_leitura = globals()[strNome]
        tuple_leitura = (var_leitura,)
        print(tuple_leitura)
        print(type(tuple_leitura))

        config = {
            'user': 'root',
            'password': '#Gf15533155708',
            'host': 'localhost',
            'database': 'Monitoll',
            'raise_on_warnings': True
        }

        cnx = mysql.connector.connect(**config)

        if cnx.is_connected():
            db_info = cnx.get_server_info()
            print('conectado', db_info)
            cursor = cnx.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados:", linha)
        
        cursor = cnx.cursor()

        

        sql = ("INSERT INTO Leitura (Leitura, DataHora, fkTorre, fkComponente) VALUES (%s, %s, %s, %s)")
        values = (var_leitura, datahora, idTorre , y)


        try:
            # Executando comando SQL   
            cursor.execute(sql, values)

            # Commit de mudanças no banco de dados
            cnx.commit()

            print("Foi insert da leitura")

        except mysql.connector.Error as err:
            cnx.rollback()
            print("Something went wrong: {}".format(err))







    def criarTabela():

        config = {
            'user': 'root',
            'password': '#Gf15533155708',
            'host': 'localhost',
            'database': 'Monitoll',
            'raise_on_warnings': True
        }

        cnx = mysql.connector.connect(**config)

        if cnx.is_connected():
            db_info = cnx.get_server_info()
            print('conectado', db_info)
            cursor = cnx.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados:", linha)

        cursor = cnx.cursor()

        query = ("SELECT `idTorre` FROM Torre " 
                "WHERE SerialID = %s;")
        try:
            # Executing the SQL command
            cursor.execute(query, (trim4SerialID,))
            print("fez o select")

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        global idTorre
        idTorre = cursor.fetchone()

        if idTorre is not None:
            print("tem id")

            # PEGAR idTORRE VIA SERIAL ID
            queryTorre = ("SELECT `idTorre` FROM Torre " 
                "WHERE SerialID = %s;")
            try:
            # Executing the SQL command
                cursor.execute(queryTorre, (trim4SerialID,))
                print("fez o select do id")

            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

            idTorre = sum(cursor.fetchone())
            print("id da torre: ", idTorre)





            # PREGAR fkCOMPONENTE
            queryComponente = ("SELECT `fkComponente` FROM Torre_Componente " 
                    "WHERE Torre_Componente.fkTorre = %s;")

            try:
                # Executing the SQL command
                cursor.execute(queryComponente, (idTorre,))
                print("fez o select")

            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

            fkComponente= cursor.fetchall()
            vet_fkComponente = numpy.asarray(fkComponente)
            print("fkComponente: ", vet_fkComponente)

            
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
                    print("fez o select")

                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))

                Codigo = cursor.fetchone()
                print("fkComponente: ", Codigo)

                def convertTuple(tup):
                    str = functools.reduce(operator.add, (tup))
                    return str

                global strCodigo
                strCodigo = convertTuple(Codigo)
                print(strCodigo)
            


                # PREGAR NOME COMPONENTE
                queryNome = ("SELECT `Nome` FROM Componente " 
                    "WHERE Componente.idComponente = %s;")

                try:
                    # Executing the SQL command
                    cursor.execute(queryNome, (y,))
                    print("fez o select")

                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))

                Nome= cursor.fetchone()
                global strNome
                strNome = convertTuple(Nome)
                print("Nome componente: ", strNome)
                print(strNome + " = " + strCodigo)
                teste()
    

        else:
            print("não tem id")
            sql = ("UPDATE Torre  SET SerialID = %s,  SO = %s, Maquina = %s, Processador = %s, Disco = %s, VelocidadeRam = %s,  fkEmpresa = %s WHERE idTorre = 101")
            values = (trim4SerialID, trim4OSnome, trim4ModeloPC, trim4ModeloCPU, trim4ModeloDR, trim4ramSpeed, 1)

            try:
                # Executando comando SQL
                cursor.execute(sql, values)

                # Commit de mudanças no banco de dados
                cnx.commit()

                print("inseriu nova torre no banco")

            except mysql.connector.Error as err:
                cnx.rollback()
                print("Something went wrong: {}".format(err))

            try:
                # Executando comando SQL
                cursor.execute(query, (trim4SerialID,))
                print("fez o select de sem id")
                idTorre = cursor.fetchone()


            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                
            print(idTorre)

        cnx.close()



    criarTabela()
    time.sleep(10)