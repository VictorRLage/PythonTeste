import subprocess
class Bibliotecas:
    def __init__(self, psutil=True, mysql_connector=True, numpy=True):

        if not psutil:
             subprocess.run('pip install psutil', shell=True)
        if not mysql_connector:
            subprocess.run('pip install mysql-connector-python', shell=True)
        if not numpy:
            subprocess.run('pip install numpy', shell=True)

