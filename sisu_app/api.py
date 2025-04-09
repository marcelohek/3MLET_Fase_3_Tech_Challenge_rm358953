
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

modelo = joblib.load("modelo_xgboost_sisu.joblib")
features = joblib.load("features_xgboost_sisu.pkl")

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
    entrada = dados.dict()  

    entrada_dummies = {
        "QT_VAGAS_CONCORRENCIA": entrada["qt_vagas"],
        f"NOME_CURSO_{entrada['nome_curso']}": 1,
        f"SIGLA_IES_{entrada['sigla_ies']}": 1,
        f"UF_CAMPUS_{entrada['uf_campus']}": 1,
        f"GRAU_{entrada['grau']}": 1,
        f"TURNO_{entrada['turno']}": 1,
        f"MOD_CONCORRENCIA_{entrada['mod_concorrencia']}": 1,
    }

    entrada_final = {col: entrada_dummies.get(col, 0) for col in features}
    df = pd.DataFrame([entrada_final])
    pred = modelo.predict(df)[0]
    return {"nota_prevista": round(float(pred), 2)}  
