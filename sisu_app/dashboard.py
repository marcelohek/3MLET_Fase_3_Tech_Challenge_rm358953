import streamlit as st
import joblib
import requests

st.set_page_config(page_title="Preditor de Nota de Corte SISU", layout="centered")

# Carregar features do modelo
features = joblib.load("features_xgboost_sisu.pkl")

def extrair_opcoes(prefixo):
    return sorted({col.replace(prefixo, "") for col in features if col.startswith(prefixo)})

# Opções extraídas do modelo treinado
cursos = extrair_opcoes("NOME_CURSO_")
ies = extrair_opcoes("SIGLA_IES_")
ufs = extrair_opcoes("UF_CAMPUS_")
graus = extrair_opcoes("GRAU_")
turnos = extrair_opcoes("TURNO_")
modalidades = extrair_opcoes("MOD_CONCORRENCIA_")

st.title("Preditor de Nota de Corte SISU")
st.markdown("Preencha os dados abaixo para obter a **nota de corte estimada**.")

curso = st.selectbox("Curso", cursos)
sigla_ies = st.selectbox("Instituição (sigla)", ies)
uf = st.selectbox("Estado (UF)", ufs)
grau = st.selectbox("Grau", graus)
turno = st.selectbox("Turno", turnos)
modalidade = st.selectbox("Modalidade de concorrência", modalidades)
qt_vagas = st.number_input("Quantidade de vagas", min_value=1, max_value=200, value=40)

if st.button("Estimar Nota de Corte"):
    payload = {
        "nome_curso": curso,
        "sigla_ies": sigla_ies,
        "uf_campus": uf,
        "grau": grau,
        "turno": turno,
        "mod_concorrencia": modalidade,
        "qt_vagas": qt_vagas
    }

    try:
        resposta = requests.post("http://localhost:8000/prever", json=payload)
        if resposta.status_code == 200:
            resultado = resposta.json()
            st.success(f"Nota prevista: **{resultado['nota_prevista']} pontos**")
        else:
            st.error("Erro na API. Verifique se ela está rodando.")
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
