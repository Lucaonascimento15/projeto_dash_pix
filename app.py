import pandas as pd
#Objetivo do projeto: criar um dashboard que 
# 1 - volume de pix por ano
# 2 - volume de pix por localidade
# 3 - TOP 10 valores de transações gerais


# Lê o arquivo CSV
df = pd.read_csv ('C:\\Users\\Lucas Santos\\Desktop\\ambiente_python\\projeto_pix\\estatistiscas_pix.csv')

# Exibe as primeiras linhas do DataFrame
print(df['AnoMes'])