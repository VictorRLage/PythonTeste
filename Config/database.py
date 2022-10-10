import mysql.connector

class Database:
    cnx = cursor = None

    def __init__(self, user, senha, host, database):
        global cnx, cursor

        cnx = mysql.connector.connect(user=user, password=senha, host=host, database=database, raise_on_warnings=True)

        if cnx.is_connected():
            db_info = cnx.get_server_info()
            print('conectado', db_info)
            cursor = cnx.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados:", linha)
            

    def inserirDadosMaquina(self, SerialID, OS, Maquina, Processador, Disco, RamSpeed):

        print("Os dados dessa maquina não estão cadastrados no sistema ")


        sql = (
            "UPDATE Torre  SET SerialID = %s,  SO = %s, Maquina = %s, Processador = %s, Disco = %s, VelocidadeRam = %s,  fkEmpresa = %s WHERE idTorre = 101")
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

        query = ("SELECT `idTorre` FROM Torre "
                 "WHERE SerialID = %s;")

        try:
            # Executando comando SQL
            cursor.execute(query, (SerialID,))
            print("fez o select de sem id")
            idTorre = cursor.fetchone()


        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        print('Dados da torre', idTorre, 'foram inseridos no banco')
