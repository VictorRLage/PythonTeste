import pyodbc
import textwrap

#Definindo o driver
driver = '{ODBC Driver 17 for SQL Server}'
# definindo server e database
server_name = 'montioll'
database_name = 'Monitoll'
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
# definindo o nome e a senha 
username = 'Monitoll'
password = 'Grupo7@123'

# definindo o banco url
connection_string = textwrap.dedent("""
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

# criando o objeto de conecxao
cnxn:pyodbc.Connection = pyodbc.connect(connection_string)


# criando um novo cursor 
crsr: pyodbc.Cursor = cnxn.cursor()

#criando execute vdd
crsr.fast_executemany= True
# definindo insert query 
insert_sql = "INSERT INTO [Perfil] (idPerfil,Cargo) VALUES(?,?)" 

# criando record 
records = [('4','Dono')]

# select 
# select_sql = " SELECT * FROM [PERFIL]"
# definindo 

#executando insert 
crsr.executemany(insert_sql, records)

# commit 
crsr.commit()


# close the connection
cnxn.close()
