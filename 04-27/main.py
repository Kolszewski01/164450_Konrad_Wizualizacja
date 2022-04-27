import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts=pd.Series(np.random.randn(1000))
ts=ts.cumsum()
#
# ts.plot()
# plt.show()


dane={'Kraj':['Belgia','Indie','Brazylia','Polska'],
      'Stolica':['Bruksela','New delhi','Brasilia','Warszawa'],
      'Populacja':[1414124,312312,12321321,123132],
      'Kontynent':['hehe','xddd','podlasie','europa']}
#
# df=pd.DataFrame(dane)
# grupa=df.groupby('Kontynent').agg({'Populacja':['sum']})
# print(grupa)
# # grupa.plot(kind='bar',xlable='Kontynent',ylabel='Populacja',
# #            rot=0,title='Populacja kontynentow')
#
#
# wykres=grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x',labelrotation=0)
# wykres.legend(loc='upper center')
# wykres.set_title('Populacja na kontynentach')
#
#
#
# plt.savefig('wykres.png')
#
# plt.show()

#
# df=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
# print(df)
#
# grupa=df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
#
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',
#            fontsize=20, figsize=(8,8), colors=['red','green'])
#
# plt.legend(loc='upper left')
#
# plt.show()

df=pd.DataFrame(ts)
print(df)
df['Średnia kroczaca']=df.rolling(window=50).mean()
df.plot()
pl