import mysql.connector

def createDB():
  """
  Função para criação do banco de dados.
  Cria o banco de dados, caso não exista, e cria as tabelas requests, responses, route, service, latencies e logs.

  Requests: request_id é a primary key, criada para a relação das tabelas na tabela logs.
  querystring e headers foram salvos como objetos json.

  Responses: response_id é a primary key, criada para a relação das tabelas na tabela logs.
  headers foi salvo como objetos json.

  Route:  route_id é a primary key, criada para a relação das tabelas na tabela logs.
  methods, paths, protocols e service foi salvo como objetos json.

  Service: service_id é a primary key, criada para a relação das tabelas na tabela logs.

  Latencies: latencies_id é a primary key, criada para a relação das tabelas na tabela logs.

  Logs: request_id, response_id, route_id, service_id e latencies_id são foreign keys de cada uma das outras tabelas.
  Além disso, logs guarda o valor de upstream_uri, client_ip e started_up, valores que faziam parte do objeto maior.
  Como o objeto authenticated_entity tinha somente um valor, optei por guardá-lo também na tabela de logs.

  :return: conexão com o database
  """

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
  )

  mycursor = mydb.cursor()

  mycursor.execute("create database if not exists me default character set utf8 default collate utf8_general_ci")

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="me"
  )

  mycursor = mydb.cursor()

  # Criação table requests, caso ainda não exista
  mycursor.execute("create table if not exists requests (request_id int not null auto_increment,method varchar(12), uri varchar(12),url varchar(255),size int,querystring longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),headers longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),primary key (request_id)) default charset = utf8")

  # Criação table responses, caso ainda não exista
  mycursor.execute("create table if not exists responses (response_id int not null auto_increment,status varchar(12),size int,headers longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),primary key (response_id)) default charset = utf8")

  # Criação table route, caso ainda não exista
  mycursor.execute("create table if not exists route (route_id int not null auto_increment,id char(56) not null,created_at varchar(56),hosts varchar(56),methods longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),paths longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),preserve_host bool,protocols longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),regex_priority tinyint,service longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(log)),strip_path bool,updated_at varchar(56),primary key (route_id)) default charset = utf8")

  # Criação table service, caso ainda não exista
  mycursor.execute("create table if not exists service (service_id int not null auto_increment,id char(36) not null,connect_timeout varchar(12),created_at varchar(56),host varchar(255),name varchar(255),path varchar(12),port int,protocol varchar(12),read_timeout varchar(12),retries int,updated_at varchar(56),write_timeout varchar(12),primary key (service_id)) default charset = utf8")

  # Criação table latencies, caso ainda não exista
  mycursor.execute("create table if not exists latencies (latencies_id int not null auto_increment,proxy int,kong int,request int,primary key (latencies_id)) default charset = utf8;")

  # Criação table logs
  mycursor.execute("create table if not exists logs (logs_id int not null auto_increment,request_id int not null,response_id int not null,consumer_id char(36) not null, route_id char(36) not null,service_id char(36) not null,latencies_id int not null,upstream_uri varchar(12),client_ip char(15) not null,started_at varchar(56),primary key (logs_id),foreign key (request_id) references requests(request_id),foreign key (response_id) references responses(response_id), foreign key (route_id) references route(route_id),foreign key (service_id) references service(service_id),foreign key (latencies_id) references latencies(latencies_id)) default charset = utf8")

  return mydb