# Testa se a função validar dados esta correta separando validos de invalidos e identifica erros de tiipo (id, agr, salary)
# e valida campos obrigatórios
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from csv_utils import validar_dados


def test_validar_dados():
    df = pd.DataFrame({
        "id": [1,"x"],
        "name": ["João", ""],
        "email": ["joaogabriel39359@email.com", ""],
        "age": [25, "abc"],
        "salary": [5000.0, "xyz"]
    })

    validos, invalidos = validar_dados(df)

# O assert len verifica a quantidade de itens

    assert len(validos) == 1
    assert len(invalidos) == 1
