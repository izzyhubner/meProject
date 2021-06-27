import mysql.connector
import json

def clean_records(mydb):
    """
    Função para caso o teste seja executado mais de uma vez, garantir que os dados serão excluídos antes de adicionar novos dados, evitando duplicidade.

    :param mydb: database a ter seus dados limpos
    """
    mycursor = mydb.cursor()
    sql = "delete from logs"
    mycursor.execute(sql)
    mydb.commit()

def request_to_db(df_request, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.
    Utiliza o json.dumps nos valores querystring e headers para passar os objetos para string.

    :param df_request: dataframe com os dados a serem carregados para a tabela Requests
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    for index, row in df_request.iterrows():
        sql = "INSERT INTO requests (method, uri, url, size, querystring, headers) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row['method'], row['uri'], row['url'], row['size'], json.dumps(row['querystring']), json.dumps(row['headers']))
        mycursor.execute(sql, val)
    mydb.commit()

def response_to_db(df_response, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.
    Utiliza o json.dumps em headers para passar o objeto para string.

    :param df_request: dataframe com os dados a serem carregados para a tabela Reponses
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    for index, row in df_response.iterrows():
        sql = "INSERT INTO responses (status, size, headers) VALUES (%s, %s, %s)"
        val = (row['status'], row['size'], json.dumps(row['headers']))
        mycursor.execute(sql, val)
    mydb.commit()

def route_to_db(df_route, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.
    Utiliza ' '.join() nos valores methods, paths e protocols para converter de lista para string.
    Utiliza o json.dumps no valor service para passar o objeto para string.

    :param df_request: dataframe com os dados a serem carregados para a tabela Route
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    for index, row in df_route.iterrows():
        sql = "INSERT INTO route (id, created_at, hosts, methods, paths, preserve_host, protocols, regex_priority, service, strip_path, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row['id'], row['created_at'], row['hosts'], ' '.join(row['methods']), ' '.join(row['paths']), row['preserve_host'], ' '.join(row['protocols']), row['regex_priority'], json.dumps(row['service']), row['strip_path'], row['updated_at'])
        mycursor.execute(sql, val)
    mydb.commit()

def service_to_db(df_service, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.

    :param df_request: dataframe com os dados a serem carregados para a tabela Service
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    for index, row in df_service.iterrows():
        sql = "INSERT INTO service (id, connect_timeout, created_at, host, name, path, port, protocol, read_timeout, retries, updated_at, write_timeout) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row['id'], row['connect_timeout'], row['created_at'], row['host'], row['name'], row['path'], row['port'], row['protocol'],
                       row['read_timeout'], row['retries'], row['updated_at'], row['write_timeout'])
        mycursor.execute(sql, val)
    mydb.commit()

def latencies_to_db(df_latencies, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.
    Utiliza str() em proxy, kong e request para passar os valores para string.

    :param df_request: dataframe com os dados a serem carregados para a tabela Latencies
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    for index, row in df_latencies.iterrows():
        sql = "INSERT INTO latencies (proxy, kong, request) VALUES (%s, %s, %s)"
        val = (str(row['proxy']), str(row['kong']), str(row['request']))
        mycursor.execute(sql, val)
    mydb.commit()

def logs_to_db(df_logs, mydb):
    """
    Função para passar os dados do dataframe para o banco de dados.
    Foi criada uma variável chamada ids para contar e registrar todas as iterações, utilizei esse valor como primary key para cada uma das tabelas (requests, responses, route, service e latencies).

    :param df_request: dataframe com os dados a serem carregados para a tabela Logs
    :param mydb: database onde os dados serão carregados
    """

    clean_records(mydb)
    mycursor = mydb.cursor()

    ids = 0

    for index, row in df_logs.iterrows():
        sql = "INSERT INTO logs (request_id, response_id, route_id, service_id, latencies_id, upstream_uri, client_ip, started_at, consumer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (ids, ids, ids, ids, ids, row['upstream_uri'], row['client_ip'], row['started_at'], row['consumer_id.uuid'])
        mycursor.execute(sql, val)
        ids += 1
    mydb.commit()