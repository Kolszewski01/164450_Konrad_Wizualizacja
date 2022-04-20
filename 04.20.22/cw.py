import numpy as np
import pandas as pd

# s=pd.Series([1,3,5.5,np.nan,'a'])
# print(s)

s1=pd.Series([10,12,8,14],index=['a','b','c','d'])
print(s1)

dane={'Kraj':['Belgia','Indie','Brazylia'],
      'Stolica':['Brulsela','New Delhi','Brasilia'],
      'Populacja':[111123313,4141412,53523523]}

df=pd.DataFrame(dane)

print(df)

#
# daty=pd.data_range('2022002',periodos=5)
# df=pd.DataFrame(np.random.ramdn(5,4), index=daty, columns=list('ABCD'))
#
#
#
iris_df=pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
#
# print(iris_df)
#
# iris_df.to_csv('nowy.csv',index=False)
# print(iris_df)
#
# xlsx=pd.ExcelFile('wyniki.xlsx')
# df=pd.read_excel(xlsx,header=0)
#
# df.to_excel('nowy.xlsx',sheet_name="arkusz.1",index=False)
#

# print(s1['a'])
# print(s1.a)
# print(df['Populacja'])
# print(df.Populacja)
#
# print(df.iloc[[0],[1]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])
#
# print('kraj: '+ df.Kraj)

# print(df.sample(1))
# print(df.sample(frac=0.5))
#
# print('')
# print(df.sample(10,replace=True))
#
#
# print(iris_df.head(10))
# print(iris_df.tail(10))
#
# print(s1[s1>10])
#
# seria=s1.copy()
# print(seria)

# seria.where(s1>10,'element nie spełnia warunku',inplace=True)

# print(seria)
# print(s1[~(s1>10)])
# print(s1[(s1<13)&(s1>8)])
# print(df[df['Populacja']>12000000])
# print(df[(df.Populacja>10000)&(df.index.isin([0,2]))])
# print(seria)

# szukaj=['Belgia','Brasilia']
# print(df.isin(szukaj))
#
# s1['e']=15
# print(s1)
# df.loc[3]='ne'
# df.loc[4]=['Polska','warszawa',32313231]
#
# print(df)
#
# df.drop(3.inplace-True)
# print(df)

df.drop('Kraj',axis=1,inplace=True)
print(df)

df['Kontynent']=['Europa','Azja','Ameryka Południowa','Europa']
print(df)
print(df.sort_values(by='Kraj'))
grupa=df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))

print(df.groupby(by='Kontynent').agg({'Populacja':['sum']}))
