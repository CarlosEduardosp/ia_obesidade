import pandas as pd
import numpy as np
from src.analise_de_dados.previsores.previsores_escalonado import Previsores_escalonado
from src.analise_de_dados.previsores.previsores2 import Previsores2
from src.analise_de_dados.previsores.previsores3 import Previsores3
from src.analise_de_dados.Chamar_algoritimo.chamar_algoritimo import chamarAlgoritimo

# Configurar pandas para comportamento futuro
pd.set_option('future.no_silent_downcasting', True)

# Ajustar a largura máxima de exibição
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# lendo o arquivo csv
df = pd.read_csv('../../obesidadeData.csv',
                     sep=',', encoding='utf-8')

# mostrando a tabela na tela com o print
#print(df.shape)

# mostra quantidade de linhas e colunas
# print(df.shape)

# mostra os tipos dos valores dentro de cada celula.
#print(df.dtypes)


# descobrir valores que aparecem pelo menos uma vez na coluna, parametro é o nome da coluna.
valores_unicos = df['MTRANS'].unique()
# print(valores_unicos)

# Transformando as variáveis categóricas nominais em variáveis categóricas ordinais
# criando um dataframe
df2 = pd.DataFrame.copy(df)
print(df2.head(10))


# tranformando as variaveis
df2['Gender'] = df2['Gender'].replace({'Male': int(0), 'Female': int(1)}).astype(int)
df2['CALC'] = df2['CALC'].replace({'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}).astype(int)
df2['FAVC'] = df2['FAVC'].replace({'no': 0, 'yes': 1}).astype(int)
df2['SCC'] = df2['SCC'].replace({'no': 0, 'yes': 1}).astype(int)
df2['SMOKE'] = df2['SMOKE'].replace({'no': 0, 'yes': 1}).astype(int)
df2['family_history_with_overweight'] = df2['family_history_with_overweight'].replace({'no': 0, 'yes': 1}).astype(int)
df2['CAEC'] = df2['CAEC'].replace({'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}).astype(int)
df2['MTRANS'] = df2['MTRANS'].replace(
    {'Walking': 0, 'Public_Transportation': 1, 'Bike': 2, 'Motorbike': 3, 'Automobile': 4}).astype(int)
df2['NObeyesdad'] = df2['NObeyesdad'].replace(
    {'Insufficient_Weight': 0, 'Normal_Weight': 1, 'Overweight_Level_I': 2, 'Overweight_Level_II': 3,
     'Obesity_Type_I': 4, 'Obesity_Type_II': 5, 'Obesity_Type_III': 6}).astype(int)
print(df2.head(55))

#print(df2.dtypes)

"""
alvo = variável que se pretende atingir (tem ou não doença cardíaca).
previsores = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas manualmente, sem escalonar.
"""
previsores = df2.iloc[:, 0:16].values
#print(previsores)

#print(previsores.shape)

# Alvo
alvo = df2.iloc[:, 16].values
#print(alvo)

# Analise de escalas dos atributos
#print(df2.describe())

"""
alvo = variável que se pretende atingir (tem ou não doença cardíaca).
previsores = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas manualmente, sem escalonar.
previsores_esc = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas, escalonada.
previsores2 = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas pelo labelencoder.
previsores2_esc = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas pelo labelencoder, escalonada.
previsores3 = conjunto de variáveis previsoras transformadas pelo labelencoder e onehotencoder, sem escalonar.
previsores3_esc = conjunto de variáveis previsoras transformadas pelo labelencoder e onehotencoder escalonada.
"""

previsores_escalonado = Previsores_escalonado(previsores)
#print(previsores_escalonado)

previsores2 = Previsores2(df)
#print(previsores2)

previsores2_escalonado = Previsores_escalonado(previsores2)
#print(previsores2_escalonado)

previsores3 = Previsores3(previsores2)
# visualizando com dataframeS
previsores3df = pd.DataFrame(previsores3)
#print(previsores3df)

previsores3_escalonado = Previsores_escalonado(previsores3)
previsores3_escdf = pd.DataFrame(previsores3_escalonado)
#print(previsores3_escdf)

# reunindo todos os previsores em uma lista.
todos_os_previsores = [
    {"id": "previsores", "previsores": previsores},
    {"id": "previsores_esc", "previsores": previsores_escalonado},
    {"id": "previsores2", "previsores": previsores2},
    {"id": "previsores2_esc", "previsores": previsores2_escalonado},
    {"id": "previsores3", "previsores": previsores3},
    {"id": "previsores3_esc", "previsores": previsores3_escalonado},
]

#salvando os arquivos no diretório designado.
#np.savetxt('/src/dados_csv/previsores.csv', previsores, delimiter=',')
#np.savetxt('/src/dados_csv/alvo.csv', alvo, delimiter=',')

# testando e avaliando com naive bayes
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=1)

# testando e avaliando com SVM - Máquinas de Vetores de Suporte
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=2)

# testando e avaliando com Regressão Logística
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=3)

# testando e avaliando com KNN - aprendizagem baseada em instâncias
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=4)

# testando e avaliando com Árvore de Decisão
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=5)

# testando e avaliando com Random Forest
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=6)

# testando e avaliando com XGBoost
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=7)

# testando e avaliando com lightGbm
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=8)

# testando e avaliando com Catboost
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=9)
