import pyodbc
import textwrap

#Definindo o driver
driver = '{ODBC Driver 17 for SQL Server}'

# definindo server 
server_name = 'monitoll'
database_name = 'Monitoll'

server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
# definindo o nome e a senha 
username = 'Monitoll'
password = 'Monitoll123'

# definindo o banco url
connection_string = textwrap.dedent("""
Driver ={driver};
Server={server};
Database={database};
Uid={username};
Pwd={password};
Encrypt=yes;
TrustedServerCertificate=no;
Connection Timeout=30;
""".format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))

# criando o objeto de conecxao
cnxn:pyodbc.Connection = pyodbc.connect(connection_string)

#criando execute vdd
crsr.fast_executemany= True

# criando um novo cursor 
crsr: pyodbc.cursor = cnxn.cursor()

# definindo insert query 
insert_query = "INSERT INTO [Torre] (SerialID, SO, Maquina, Processador, Disco, VelocidadeRam, fkEmpresa) VALUES(?,?,?,?,?,?,?)"
records=[] 

# definindo 

#executando insert 
crsr.executemany(insert_query, records)

# commit 
crsr.commit()

# close the connection
cnxn.close()
