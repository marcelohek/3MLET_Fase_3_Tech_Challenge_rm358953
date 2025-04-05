
import streamlit as st
import requests

st.set_page_config(page_title="Preditor de Nota de Corte SISU", layout="centered")

st.title("Preditor de Nota de Corte SISU")
st.markdown("Preencha os dados abaixo para obter a **nota de corte estimada**.")

curso = st.selectbox("Curso", ["Engenharia Civil", "Medicina", "Direito", "Administração"])
sigla_ies = st.selectbox("Instituição (sigla)", ["UFRJ", "USP", "UFBA", "UFMG"])
uf = st.selectbox("Estado (UF)", ["RJ", "SP", "BA", "MG"])
grau = st.selectbox("Grau", ["Bacharelado", "Licenciatura", "Tecnológico"])
turno = st.selectbox("Turno", ["Integral", "Noturno", "Matutino"])
modalidade = st.selectbox("Modalidade de concorrência", ["AC", "L1", "L2", "L5"])
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
