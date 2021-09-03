# -*- coding: utf-8 -*-
"""JovenscomAids.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dT6_qDhndfvmkGEpCqIsreATvTXunj_C
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from matplotlib import pyplot as plt

#Dados de Jovens com AIDS no Brasil em 2019.
df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/DIO - Análise de Dados com Pandas e Python/eixo5_jovensaids_2019.csv')

#Quantas linhas e colunas tem nesse dataset
df.shape

#Exibindo todo o dataset
df.head(27)

#Verificando se há dados em branco/nulos
df.isnull().sum()

df.describe()

rj= df.loc[df["Nome"]=="Rio de Janeiro"]
rj.head()

sp=df.loc[df["Nome"]=="São Paulo"]
sp.head()

#Os 5 primeiros Estados mais contaminados com AIDS no Brasil.
QntGeralAids = df.sort_values("Total", ascending=False).head(5)
QntGeralAids.head(5)

#Os 3 Estado com mais homens com Aids
df.nlargest(3,"Masculino")

#Os 3 Estados com menos homens com aids
df.nsmallest(3,"Masculino")

#Os 3 Estados com mais mulheres com aids
df.nlargest(3,"Feminino")

#Os 3 Estados com menos mulheres com aids
df.nsmallest(3,"Feminino")

#Os cinco Estados com mais homens contaminados em proporção à sua população total.
df.nlargest(5,"Masculino(%)")

#Os cinco Estados com menos homens contaminados em proporção à sua população total.
df.nsmallest(5,"Masculino(%)")

#Os cinco Estados com mais mulheres contaminadas em proporção à sua população total.
df.nlargest(5,"Feminino(%)")

#Os cinco Estados com menos mulheres contaminadas em proporção à sua população total.
minFemP =df.nsmallest(5,"Feminino(%)")

#Estabelecento métrica
Homens = df.Masculino.sum()
Mulheres = df.Feminino.sum()
total = df.Total.sum()
#Homens e mulheres em porcentagem
PorcentagemHom = (Homens *100)/Total
PorcentagemFem = (Mulheres *100)/Total

#Visualizando o grupo mais afetado com AIDS
labels = 'Masculino', 'Feminino'
sizes = [ Homens, Mulheres,]
fig1, ax1 = plt.subplots();
explode = (0,0.1); 
ax1.pie(sizes,explode = explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90);
ax1.axis('equal');

#Estados com mais Homens infectados
labels = 'SP', 'RJ', 'PA'
sizes = [713, 319, 235,]
explode = [0.1,0,0]
fig2, ax2 = plt.subplots();
ax2.pie(sizes,labels=labels,explode = explode, autopct='%1.1f%%',shadow=True,startangle=90);
ax2.axis('equal');

#Estados com mais Mulheres infectadas
labels = 'RS', 'RJ', 'SP'
sizes = [137,133,133]
explode = [0.1,0,0]
fig3, ax3 = plt.subplots();
ax3.pie(sizes,labels=labels,explode = explode, autopct='%1.1f%%',shadow=True,startangle=90);
ax3.axis('equal');

#Visualizando os TOP Estados Mais Infectados
labels = 'SP','RJ','PA','RS','AM'
sizes = [ 846, 452,347,320,284]
fig4, ax4 = plt.subplots();
explode = (0.1,0,0,0,0); 
ax4.pie(sizes,explode = explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90);
ax4.axis('equal');