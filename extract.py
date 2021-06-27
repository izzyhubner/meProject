import json
import pandas as pd

def json_to_df(file):
    """
    Função para ler um arquivo json.txt com um objeto por linha e salvá-lo em um dataframe.
    A função utiliza uma lista auxiliar para a junção dos objetos json, que são concatenados a cada linha com o auxílio do json.loads. No final, essa lista é transformada em um dataframe.

    :param file: arquivo json.txt
    :return: dataframe com os dados do json
    """
    aux = []

    with open(file) as f:
        for line in f:
            j_content = json.loads(line)
            aux.append(j_content)

    df = pd.DataFrame(aux)
    return df