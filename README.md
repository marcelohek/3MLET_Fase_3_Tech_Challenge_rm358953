# 3MLET_Fase_3_Tech_Challenge_rm358953

### Marcelo Hissao Ekami - RM 358953

Este trabalho tem como objetivo a construção de um dashboard que permite estimar a nota de corte do SISU (Sistema de Seleção Unificada) a partir de dados históricos e um modelo de machine learning.

### Fonte de dados
Os dados foram obtidos do Portal de Dados Abertos do Ministério da Educação.
https://dadosabertos.mec.gov.br/sisu

### Análise dos dados e criação do modelo de Machine Learning
As operações realizadas podem ser reproduzidas no notebook:
https://colab.research.google.com/drive/1Wc37W6QVB8bbHFJYEbF3RgMKQvm7OAxi#scrollTo=PsR32yFZXlj0
O modelo treinado é salvo como modelo_xgboost_sisu.joblib
As features usadas para o treino são salvas como features_xgboost_sisu.pkl

### Criação de API e Dashboard
A API que realiza a previsão da nota de corte foi criada utilizando o framework FastAPI e possui o endpoint /prever que recebe dados via JSON e retorna a nota de corte prevista.
Execução local com Uvicorn:
uvicorn api:app --host 0.0.0.0 --port 8000
http://localhost:8000/docs

O Dashboard permite selecionar os parâmetros (curso, UF, turno, vagas, etc) e faz a chamada para a API.
Execução local :
streamlit run dashboard.py
http://localhost:8501

As dependências de ambos estão listadas no requirements.txt .

### Deploy da aplicação
Foi realizado o deploy da API e do Dashboard em uma instância EC2 na AWS. 
Link para dashboard hospedado na AWS: http://54.208.50.208:8501/
