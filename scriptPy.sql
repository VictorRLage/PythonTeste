create database Monitoll;
use Monitoll;

CREATE TABLE Perfil(
idPerfil INT PRIMARY KEY,
Permissoes CHAR(3)
);

CREATE TABLE Empresa(
idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(45),
CNPJ CHAR(14),
Email VARCHAR(40)
)AUTO_INCREMENT = 1;

CREATE TABLE Usuario(
idUsuario INT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(45),
CPF CHAR(11),
Email VARCHAR(40),
Senha VARCHAR(20),
fkPerfil INT,
FOREIGN KEY (fkPerfil) REFERENCES Perfil(idPerfil),
fkEmpresa INT,
FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
)AUTO_INCREMENT = 1;

CREATE TABLE Torre(
idTorre INT PRIMARY KEY,
SerialID VARCHAR(45),
SO VARCHAR(45),
Maquina VARCHAR(45),
Processador VARCHAR(45),
Disco VARCHAR(45),
VelocidadeRam VARCHAR(10),
fkEmpresa Int,
FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
);

CREATE TABLE Componente(
idComponente INT PRIMARY KEY,
Nome VARCHAR(45),
Codigo VARCHAR(100)
)AUTO_INCREMENT = 1;

CREATE TABLE Torre_Componente(
fkTorre INT,
fkComponente INT,
FOREIGN KEY (fkTorre) REFERENCES Torre(idTorre),
FOREIGN KEY (fkComponente) REFERENCES Componente(idComponente),
PRIMARY KEY (fkTorre, fkComponente)
);

CREATE TABLE Leitura(
idLeitura INT PRIMARY KEY AUTO_INCREMENT,
Leitura VARCHAR(50),
DataHora CHAR(19),
fkTorre INT,
fkComponente INT,
FOREIGN KEY (fkTorre) REFERENCES Torre(idTorre),
FOREIGN KEY (fkComponente) REFERENCES Componente(idComponente)
)AUTO_INCREMENT = 1000;



INSERT INTO Perfil VALUES (1, 'Dev'),
						  (2, 'Adm'),
                          (3, 'Fun');
INSERT INTO Empresa VALUES (null, 'EmpTeste', '99999999999999', 'empteste123@gmail.com');
INSERT INTO Usuario VALUES (null,"Pedro Neto",null,"pedro.cordeironeto@sptech.school","123",1,NULL),
                                  (null,"Victor Lage",null,"victorlage3000@gmail.com","123",1,NULL),
                                  (null,"Renato Tierno",null,"renato.tierno@sptech.school","123",1,NULL),
                                  (null,"Emerson Santos",null,"emerson.santos@sptech.school","123",1,NULL),
                                  (null,"Gabriela Romanini",null,"gabriela.silva@sptech.school","123",1,NULL),
                                  (null,"Luigi Ceolin",null,"luigi.ceolin@sptech.school","123",1,NULL),
                                  (null, "Adm EmpTeste",null, "admempteste@gmail.com",'123', 2, 1),
                                  (null, "Fun EmpTeste",null, "funempteste@gmail.com",'123', 3, 1);
INSERT INTO Torre (idTorre, fkEmpresa) values  (101,1),
                                               (102,1),
                                               (103,1),
                                               (104,1),
                                               (105,1);
INSERT INTO Componente VALUES (0, null, null),
							   (2, 'Processadores_qtd','psutil.cpu_count(logical=True)'),
							   (3, 'ram_total','round((psutil.virtual_memory() [0] / 10**9), 4)'),
                               (4, 'ram_uso', 'round((psutil.virtual_memory() [3] / 10**9), 4)'),
                               (5,'ram_uso_porcentagem','round((psutil.virtual_memory() [2]), 1)'),
                               (6,'disco_total','round((psutil.disk_usage("/")[0] / 10**12), 3)'),
                               (7,'disco_uso','round((psutil.disk_usage("/")[1] / 10**12), 3)'),
                               (8,'disco_livre','round((psutil.disk_usage("/")[2] / 10**12), 3)'),
                               (9,'disco_uso_porcentagem','psutil.disk_usage("/")[3]'),
                               (10,'pacotes_enviados','round((psutil.net_io_counters(pernic=False, nowrap=True) [2] / 1024), 2)'),
                               (11,'pacotes_recebidos','round((psutil.net_io_counters(pernic=False, nowrap=True) [3] / 1024), 2)');
INSERT INTO Torre_Componente (fkTorre,fkComponente) values  (101, 2),
	   													         (101, 3),
                                                              (101, 4),
                                                              (101, 5),
                                                              (101, 6),
                                                              (101, 7),
                                                              (101, 8),
                                                              (101, 9),
                                                              (101, 10),
                                                              (101, 11),
                                                              (102, 3),
                                                              (102, 4),
                                                              (102, 5),
                                                              (103, 6),
                                                              (103, 7),
                                                              (103, 8),
                                                              (103, 9),
                                                              (104, 10),
                                                              (104, 11),
                                                              (105, 2);
-- INSERT INTO TORRE_COMPONENTES VALUES ();
select * from Torre;
select * from Torre_Componente;
select * from Leitura;
-- UPDATE Torre  SET SerialID = 'WERWTDS2' WHERE idTorre = 101;

CREATE USER 'tecnico'@'localhost' IDENTIFIED BY 'urubu100';
GRANT ALL ON Monitoll.* TO 'tecnico'@'localhost';


