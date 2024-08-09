# Projeto Integrado de I.A

## 📚 Sobre o projeto
O seguinte repositório foi criado com o objetivo de apresentar uma solução para o Projeto Integrado proposto na Pós Graduação de Inteligência Artificial da UNA.

O projeto trata-se de um caso de uso para aplicar o modelo <b>KNeightborsClassifier</b> no problema de diagnóstico da dengue.

## O problema... 🤔
<i>O texto abaixo trata-se do contexto apresentado para a prática do Projeto Integrado.</i> 💬 

1) Para realizarmos um projeto de mineração de dados, o primeiro é selecionar a base de dados e explorar dos dados desta base, no intuito de obtermos um entendimento inicial sobre o problema. Diante disto, utilize a biblioteca Pandas do Python para criar um <i>Data Frame</i> a partir da base de dados da dengue disponibilizada e exiba os 5 primeiros elementos deste conjunto usando o comando <i>head()</i>.

2) O segundo passo de um projeto de mineração de dados é o da transformação dos dados para posterior utilização no modelo de aprendizagem. 
Para o problema de diagnóstico da dengue será utilizado o modelo <b>KNeighborsClassifier</b>. Para usar este modelo, transforme os registros que possuem os valores ‘sim’ e ‘nao’ da base de dados da dengue em binários 1 e 0, respectivamente. Exiba os registros atualizados utilizando o comando head() da biblioteca Pandas.

3) Logo após a transformação, tem-se, finalmente, o passo de mineração de dados. Para esta etapa, divida a base de dados da dengue em treinamento e teste. Logo após, selecione o algoritmo <i>KNeighborsClassifier()</i>, utilize o comando fit para treinar o modelo e o comando predict para aplicar o método de predição. 
Apresente a matriz de confusão e a acurácia do modelo.  


## ... A SOLUÇÃO! 😍
O código completo da solução encontra-se no arquivo <i>main.py</i> e pode ser executado com o comando <code>py main.py</code>.

### Resultado obtido

A matriz de confusão mostrou que o modelo fez 4 previsões no total, das quais 3 foram corretas (2 previsões corretas de "não dengue" e 1 previsão correta de "dengue").
A acurácia foi de 0.75, o que significa que 75% das previsões foram corretas.



## Capturas de tela 📸

<b>1. Carregar a base de dados seleciona e explorar os dados</b><br>
<img src="https://github.com/lucasfrag/UNA-PI-IA/blob/main/Screenshots/Screenshot_01.jpg" style="height: 150px">

<b>2. Transformar os valores da base de dados</b><br>
<img src="https://github.com/lucasfrag/UNA-PI-IA/blob/main/Screenshots/Screenshot_02.jpg" style="height: 150px">

<b>3. Mineração de dados</b><br>
<img src="https://github.com/lucasfrag/UNA-PI-IA/blob/main/Screenshots/Screenshot_03.jpg" style="height: 150px">


## Construído com...
- Python
- Pandas
- scikit-learn
