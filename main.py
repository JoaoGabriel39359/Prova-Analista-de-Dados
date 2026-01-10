from fastapi import FastAPI, UploadFile, File
import pandas as pd

from csv_utils import validar_dados
from db_utils import salvar_funcionarios, ler_funcionarios

app = FastAPI(title="Data Ingestion API")


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file, sep=",")

    validos, invalidos = validar_dados(df)

    if not validos.empty:
        salvar_funcionarios(validos)

    return {
        "registros_validos": len(validos),
        "registros_invalidos": len(invalidos),
        "invalidos": invalidos.to_dict(orient="records")
    }


@app.get("/funcionarios")
def get_funcionarios():
    df = ler_funcionarios()
    return df.to_dict(orient="records")

# dê "uvicorn main:app --reload" para rodar o código 
# após copie "http://127.0.0.1:8000/docs" e cole na sua url para utilizar a API.

