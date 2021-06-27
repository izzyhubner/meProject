import pandas as pd
import mysql.connector

def generate_results(mydb):
  """
  Recebe o mydb para as funções mysql e gera um csv para cada output solicitado no teste.

  :param mydb: database a ser utilizado para a geração dos csvs
  """
  # Requisições por consumidor
  consumer_requests = pd.read_sql('select consumer_id, count(*) as requests from logs group by consumer_id;', con=mydb)
  consumer_requests.to_csv('consumer_requests.csv', index=False)

  # Requisições por serviço
  service_requests = pd.read_sql('select service.id as service_id, count(*) as requests from service group by service.id;', con=mydb)
  service_requests.to_csv('service_requests.csv', index=False)

  # Tempo médio de proxy, kong e requests por serviço
  service_average = pd.read_sql('select service.id as service_id, avg(latencies.proxy) as average_proxy, avg(latencies.kong) as average_kong, avg(latencies.request) as average_request from latencies inner join service on service_id = latencies_id group by service.id;', con=mydb)
  service_average.to_csv('service_average.csv', index=False)