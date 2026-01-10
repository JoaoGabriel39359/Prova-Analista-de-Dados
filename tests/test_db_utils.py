#Esse é un teste de inserção de dados no banco ele verifica se os dado validos foram salvos corretamente e podem ser recuperados

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from db_utils import salvar_funcionarios, ler_funcionarios


def test_db_insert():
    df = pd.DataFrame({
        "id": [1000],
        "name": ["Teste DB"],
        "email": ["db@test.com"],
        "age": [25],
        "salary": [3000.0]
    })

    salvar_funcionarios(df)

    resultado = ler_funcionarios()

    assert 1000 in resultado["id"].values
