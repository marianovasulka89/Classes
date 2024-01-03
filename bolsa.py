# -*- coding: utf-8 -*-
"""
Spyder Editor

Laboratorio de datos, 2do cuatrimestre 2023, visualizacion.

docente: Mariano Vasulka
"""

#vamos a "ver" para decidir cosas...

import pandas as pd

import seaborn as sns

from matplotlib import pyplot as plt

df = pd.read_csv('/home/mariano/Documents/Docencia/Labo_Datos/prices.csv')

print(df.shape , df.columns)

#queiro ver que empresas estan...

print(df['symbol'].unique())

#quiero comprar alguna accion que me haga ganar platapor ejemplo...'SJM'

#voy a ganar plata??

print(df[df['symbol']=='SJM'])

#'AMZN'??

print(df[df['symbol']=='AMZN'])

#como veran, depende de un monto de cosas, no??

#cual es mi objetivo?? en cuanto tiempo?  pero....

#compro o no compro???

df[(df['symbol']=='AMZN') & (df['date']>='2016-12-13') & (df['date']<='2016-12-23')]

#y ahora????

df[(df['symbol']=='AMZN') & (df['date']>='2016-12-13') & (df['date']<='2016-12-16')]

#en esta franja??

df[(df['symbol']=='AMZN') & (df['date']>='2016-12-16') & (df['date']<='2016-12-20')]

#se dan cuenta que mirar el df es medio un embole no??

#habra algo mejor que hacer??


subibaja = df[(df['symbol']=='AMZN') & (df['date']>='2016-12-13') & (df['date']<='2016-12-23')]
fig_subibaja = plt.figure()
sns.lineplot(x = subibaja['date'] , y = subibaja['close'])
plt.show(fig_subibaja)
plt.close()
bear = df[(df['symbol']=='AMZN') & (df['date']>='2016-12-13') & (df['date']<='2016-12-16')]
fig_bear = plt.figure()
sns.lineplot(x = bear['date'] , y = bear['close'])
plt.show()
plt.close()
bull = df[(df['symbol']=='AMZN') & (df['date']>='2016-12-16') & (df['date']<='2016-12-20')]
fig_bull = plt.figure()
sns.lineplot(x = bull['date'] , y = bull['close'])
plt.show(fig_bull)
plt.close()
##########
###spoiler alert, idea de como resolver ejercicio complejo de la guia
##########

#recorte un periodo de tiempo de la accion que yo quize

df2 = df[(df['symbol']=='AMZN') & (df['date']>='2010-01-04') & (df['date']<='2010-12-31')]


#la idea es graficar en ese periodo el precio de apertura y cierrem,
# y poder analizar la tendencia, vale jugar con tamanio de figura
#y tamanios de fuente, con menos o mas fechas

fig_open_close = plt.figure()

fig_open_close.add_subplot(1,1,1)

sns.lineplot(data = df2 , x = 'date' , y = 'open' , color = 'r')

sns.lineplot(data = df2 , x = 'date' , y = 'close')

plt.xticks(rotation = 90, fontsize = 1.8)

plt.show()

plt.close()