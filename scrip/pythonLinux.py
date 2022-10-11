import os
import subprocess

# Bloco verifcar bibliotecas instaladas
verificacao_psutil_byte = subprocess.check_output('''pip list | grep 'psutil' | uniq''', shell=True)
verificacao_psutil_str = verificacao_psutil_byte.decode('UTF-8')
verificacao_mysql_connector_byte = subprocess.check_output('''pip list | grep 'mysql-connector' | uniq''', shell=True)
verificacao_mysql_connector_str = verificacao_mysql_connector_byte.decode('UTF-8')
verificacao_numpy_byte = subprocess.check_output('''pip list | grep 'numpy' | uniq''', shell=True)
verificacao_numpy_str = verificacao_numpy_byte.decode('UTF-8')
verificacao_numpy_byte = subprocess.check_output('''pip list | grep 'numpy' | uniq''', shell=True)
verificacao_numpy_str = verificacao_numpy_byte.decode('UTF-8')

verificacao_psutil = False
verificacao_mysql_connector = False
verificacao_numpy = False

# Bloco setar  Boolean da bibliotecas
if (verificacao_psutil_str == ''):
    verificacao_psutil = True
if (verificacao_mysql_connector_str == ''):
    verificacao_mysql_connector = True
if (verificacao_numpy_str == ''):
    verificacao_numpy = True

def Bibliotecas(psutil, mysql_connector, numpy):
        if psutil:
             subprocess.run('pip install psutil', shell=True)
        if mysql_connector:
            subprocess.run('pip install mysql-connector', shell=True)
            subprocess.run('pip install mysql-connector-python', shell=True)
        if numpy:
            subprocess.run('pip install numpy', shell=True)
        

Bibliotecas(verificacao_psutil, verificacao_mysql_connector,verificacao_numpy)
exec(open('captura.py').read())