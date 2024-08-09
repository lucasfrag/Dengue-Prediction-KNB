import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


# Carregar a base de dados
df = pd.read_csv('arq_dengue.csv', delimiter=';')

# Transformer os valores "não/sim" em 0/1 e exibir os primeiros registros
df = df.replace({'sim':1, 'nao':0})
print(df.head())

# Mineração de dados

# Separar os caracteres (x) e o alvo (y)
x = df.drop(['paciente', 'dengue'], axis=1) # remover paciente e dengue
y = df['dengue'] # dengue é o alvo

# Dividir a base de dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Inicializar o classificador KNeighborsClassifier
model = KNeighborsClassifier()

# Treinar o modelo
model.fit(x_train, y_train)

# Fazer previsões
y_pred = model.predict(x_test)

# Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(cm)

# Acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")