import pandas as pd

def request_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Requests.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Requests
    """
    df_request = pd.json_normalize(df['request'], max_level=0)
    return df_request

def response_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Responses.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Responses
    """
    df_response = pd.json_normalize(df['response'], max_level=0)
    return df_response

def route_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Route.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Route
    """
    df_route = pd.json_normalize(df['route'], max_level=0)
    return df_route

def service_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Service.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Service
    """
    df_service = pd.json_normalize(df['service'], max_level=0)
    return df_service

def latencies_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Latencies.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Latencies
    """
    df_latencies = pd.json_normalize(df['latencies'], max_level=0)
    return df_latencies

def logs_table(df):
    """
    Faz a transformação do dataframe com todos os jsons e gera um dataframe somente para a tabela Logs.
    max_level foi setado como 0 para que os objetos dentro de request permanecessem como objetos.

    authenticated_entity, por ter somente consumer_id, foi normalizado e concatenado com o restante dos valores de logs.

    :param df: dataframe com todos os jsons
    :return: dataframe para a tabela Logs
    """
    df_logs = df.filter(['upstream_uri','client_ip','started_at'], axis=1)

    df_auth = pd.json_normalize(df['authenticated_entity'])
    df_logs = pd.concat([df_logs, df_auth], axis=1)
    return df_logs