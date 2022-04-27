import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1 ZAD

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
#
# grupa=df.groupby('Rok').agg({'Liczba':['sum']})
# grupa.plot(kind='bar',subplots=True,legend='False')
#
# plt.legend(loc='upper left')
#
# plt.show()
#
# print(grupa)

# 2 ZAD
#
# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
#
# grupa=df.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind='bar',subplots=True,legend='False')
#
# plt.legend(loc='upper left')
#
# plt.show()
#
# print(grupa)


# 3 ZAD

# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
#
# df = df[(df['Rok'] >= 2012) & (df['Rok'] <= 2017)]
#
# grupa=df.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',legend='False')
#
# plt.legend(loc='upper left')
#
# plt.show()
#
# print(grupa)

# 4 ZAD



df=pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df)


grupa=df.groupby('Sprzedawca').agg({'Utarg':['sum']})
grupa.plot(kind='bar',,xlable='Sprzedawca',ylabel='Utarg',
         legend='False',rot=0,)

plt.legend(loc='upper left')

plt.show()

print(grupa)


