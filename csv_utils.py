#Separação de tudo que é pandas e csv
import pandas as pd

COLUNAS_ESPERADAS = ["id", "name", "email", "age", "salary"]

def validar_dados(tabela_funcionario: pd.DataFrame):
    df = tabela_funcionario.copy()

    # valida cabeçalho
    if list(df.columns) != COLUNAS_ESPERADAS:
        raise ValueError(f"Cabeçalho inválido. Esperado: {COLUNAS_ESPERADAS}")

    # Converter para númerico
    df["id_num"] = pd.to_numeric(df["id"], errors="coerce")
    df["age_num"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary_num"] = pd.to_numeric(df["salary"], errors="coerce")

    def validar_linha(row):
        errors = []

        if pd.isna(row["id_num"]) or not float(row["id_num"]).is_integer():
            errors.append("id inválido")

        if pd.isna(row["age_num"]) or not float(row["age_num"]).is_integer():
            errors.append("age inválido")

        if pd.isna(row["salary_num"]) or not float(row["age_num"]).is_integer():
            errors.append("salary inválido")

        if pd.isna(row["name"]) or str(row["name"]).strip() == "":
            errors.append("name vazio")

        if pd.isna(row["email"]) or str(row["email"]).strip() == "":
            errors.append("email vazio")

# Retorna None se a linha for válida,
# ou uma string com os erros encontrados se for inválida

        return " | ".join(errors) if errors else None

    df["erro_validacao"] = df.apply(validar_linha, axis=1)

    validos = df[df["erro_validacao"].isna()].copy()
    invalidos = df[df["erro_validacao"].notna()].copy()

    return validos, invalidos

