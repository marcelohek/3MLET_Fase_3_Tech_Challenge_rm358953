
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

modelo = joblib.load("modelo_xgboost_sisu.joblib")

features = [
    'QT_VAGAS_CONCORRENCIA',
    'NOME_CURSO_Engenharia Civil',
    'SIGLA_IES_UFRJ',
    'UF_CAMPUS_RJ',
    'GRAU_Bacharelado',
    'TURNO_Noturno',
    'MOD_CONCORRENCIA_AC'
]

app = FastAPI()

class EntradaDados(BaseModel):
    nome_curso: str
    sigla_ies: str
    uf_campus: str
    grau: str
    turno: str
    mod_concorrencia: str
    qt_vagas: int

@app.post("/prever")
def prever_nota(dados: EntradaDados):
    entrada_dict = {
        "QT_VAGAS_CONCORRENCIA": dados.qt_vagas,
        f"NOME_CURSO_{dados.nome_curso}": 1,
        f"SIGLA_IES_{dados.sigla_ies}": 1,
        f"UF_CAMPUS_{dados.uf_campus}": 1,
        f"GRAU_{dados.grau}": 1,
        f"TURNO_{dados.turno}": 1,
        f"MOD_CONCORRENCIA_{dados.mod_concorrencia}": 1,
    }

    entrada_final = {col: entrada_dict.get(col, 0) for col in features}
    df = pd.DataFrame([entrada_final])
    pred = modelo.predict(df)[0]
    return {"nota_prevista": round(pred, 2)}
