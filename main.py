import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd 

# Carregar a base de dados
df = pd.read_csv('arq_dengue.csv', delimiter=';')

# Transformer os valores "não/sim" em 0/1 e exibir os primeiros registros
df = df.replace({'sim':1, 'nao':0})
print(df.head())


