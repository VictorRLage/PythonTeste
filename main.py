import subprocess
from Config.database import Database
from Config.bibliotecas import Bibliotecas



verificacao_psutil_byte = subprocess.check_output('''pip list | grep 'psutil' | uniq''', shell=True)
verificacao_psutil_str = verificacao_psutil_byte.decode('UTF-8')
verificacao_mysql_connector_byte = subprocess.check_output('''pip list | grep 'mysql-connector-python' | uniq''', shell=True)
verificacao_mysql_connector_str = verificacao_mysql_connector_byte.decode('UTF-8')
verificacao_numpy_byte = subprocess.check_output('''pip list | grep 'numpy' | uniq''', shell=True)
verificacao_numpy_str = verificacao_numpy_byte.decode('UTF-8')


if (verificacao_psutil_str != ''):
    verificacao_psutil = False
if (verificacao_mysql_connector_str != ''):
    verificacao_mysql_connector = False
if (verificacao_numpy_str != ''):
    verificacao_numpy = False

verificacao_bibliotecas=Bibliotecas(verificacao_psutil, verificacao_mysql_connector,verificacao_numpy)

mysql=Database('root','#Gf15533155708','localhost','Monitoll')
teste = inserirDadosMaquina('asdadasd', 'asdadasd', 'asdasdasd', 'asdasdad', 'sdasd', 2400)
