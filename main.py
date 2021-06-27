import create_db_structure
import extract
import transform
import load
import CSVOutput

"""
Criar banco de dados (consultar script create_db_structure.py para mais informações
mydb será utilizado para carregar os dataframes para o banco de dados e na geração dos csvs
"""
mydb = create_db_structure.createDB()

"""
Extrair json para dataframe (consultar script extract.py para mais informações)
#df será utilizado para a transformação e criação dos dataframes de cada tabela
"""
df = extract.json_to_df('logs.txt')

"""
Transformar dataframe em outros 6 dataframes (consultar script transform.py para mais informações)
Cada um dos dataframes normalizados servirá de input para as funções de loading
"""
df_request = transform.request_table(df)
df_response = transform.response_table(df)
df_route = transform.route_table(df)
df_service = transform.service_table(df)
df_latencies = transform.latencies_table(df)
df_logs = transform.logs_table(df)

"""
Carregar cada um dos dataframes para o banco de dados (consultar script load.py para mais informações)
"""
load.request_to_db(df_request, mydb)
load.response_to_db(df_response, mydb)
load.route_to_db(df_route, mydb)
load.service_to_db(df_service, mydb)
load.latencies_to_db(df_latencies, mydb)
load.logs_to_db(df_logs, mydb)

"""
Gerar csvs (consultar script CSVOutput.py para mais informações)
"""
CSVOutput.generate_results(mydb)