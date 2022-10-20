import os
import subprocess
import datetime

# Bloco verificar bibliotecas instaladas
verificacao_psutil_byte = subprocess.check_output('''pip list | grep 'psutil' | uniq''', shell=True)
verificacao_psutil_str = verificacao_psutil_byte.decode('UTF-8')
verificacao_pyodbc_byte = subprocess.check_output('''pip list | grep 'pyodbc' | uniq''', shell=True)
verificacao_pyodbc_str = verificacao_pyodbc_byte.decode('UTF-8')
verificacao_numpy_byte = subprocess.check_output('''pip list | grep 'numpy' | uniq''', shell=True)
verificacao_numpy_str = verificacao_numpy_byte.decode('UTF-8')
verificacao_textwrap3_byte = subprocess.check_output('''pip list | grep 'textwrap3' | uniq''', shell=True)
verificacao_textwrap3_str = verificacao_textwrap3_byte.decode('UTF-8')

# Bloco verificar driver odbc 
verificacao_driver_byte = subprocess.check_output(''' odbc -q -d -n | grep  '[ODBC Driver 18 for SQL Server]' | uniq''', shell=True )
verificacao_driver_str = verificacao_driver_byte.decode('UTF-8')
verificacao_mssql_byte = subprocess.check_output(''' odbc -q -d -n | grep  '[ODBC Driver 18 for SQL Server]' | uniq''', shell=True )
verificacao_mssql_str = verificacao_mssql_byte.decode('UTF-8')
verificacao_unix_byte = subprocess.check_output(''' odbc -q -d -n | grep  '[ODBC Driver 18 for SQL Server]' | uniq''', shell=True )
verificacao_unix_str = verificacao_unix_byte.decode('UTF-8')

verificacao_psutil = False
verificacao_pyodbc = False
verificacao_numpy = False
verificacao_textwrap3 = False
verificacao_driver = False
verificacao_mssql = False
verificacao_unix = False


# Bloco setar  Boolean das bibliotecas
if (verificacao_psutil_str == ''):
    verificacao_psutil = True
if (verificacao_pyodbc_str == ''):
    verificacao_pyodbc = True
if (verificacao_numpy_str == ''):
    verificacao_numpy = True
if (verificacao_textwrap3_str == ''):
    verificacao_textwrap3 = True

# Bloco setar Boolean dos Drivers    
if (verificacao_driver_str == ''):
    verificacao_driver_str = True
if (verificacao_mssql_str == ''):
    verificacao_mssql = True
if (verificacao_unix_str == ''):
    verificacao_unix = True

def Bibliotecas(psutil, pyodbc, numpy, textwrap3):
        if psutil:
             subprocess.run('pip install psutil', shell=True)
        if pyodbc:
            subprocess.run('pip install pyodbc', shell=True)
        if numpy:
            subprocess.run('pip install numpy', shell=True)
        if textwrap3:
            subprocess.run('pip install -U textwrap3', shell=True)

def Drivers(driver, mssql, unix):
        if driver:
            subprocess.run('sudo su', shell=True)
            subprocess.run('curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -', shell=True)
            subprocess.run('curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list', shell=True)
            subprocess.run('sudo apt update', shell=True)
            subprocess.run('sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18', shell=True)
        if mssql:
            subprocess.run('sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18', shell=True)
        if unix:
            subprocess.run('sudo apt-get install -y unixodbc-dev', shell=True)    

Bibliotecas(verificacao_psutil, verificacao_pyodbc, verificacao_numpy, verificacao_textwrap3)
Drivers(verificacao_driver, verificacao_mssql, verificacao_unix)
exec(open('teste2.py').read())