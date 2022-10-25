sudo apt install python-is-python3
sudo apt install python3-pip
pip install psutil
pip install pyodbc
pip install numpy
pip install -U textwrap3
sudo su 
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
sudo apt-get install -y unixodbc-dev
