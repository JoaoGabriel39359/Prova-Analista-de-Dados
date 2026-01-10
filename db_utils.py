#Criei o db_utils.py para facilitar manutenção e troca de banco de dados.”
#Código do banco de dados
from sqlalchemy import create_engine
import pandas as pd

DB_URL = "sqlite:///funcionarios_lifemed.db"

def get_engine():
    return create_engine(DB_URL)


def salvar_funcionarios(tabela_funcionario_validos: pd.DataFrame):
    engine = get_engine()

    colunas_finais = ["id", "name", "email", "age", "salary"]

    tabela_banco = tabela_funcionario_validos[colunas_finais].copy()

    tabela_banco.to_sql(
        name="funcionarios",
        con=engine,
        if_exists="append",
        index=False
    )


def ler_funcionarios():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM funcionarios", engine)
