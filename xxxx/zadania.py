import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

#Zadanie 1.

x_zadanie1 = np.linspace(15, 30, 30)
y_zadanie1 = np.tan(x) / (np.sin(x) + x)
plt.plot(x, y, "r-")
plt.title("wykres tan(x) / (sin(x) + x)")
plt.xlim(15, 30)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show()

#Zadanie 2.

plt.subplot(3, 2, 4)
plt.title("Pierwszy wykres")
plt.ylabel("wynik funkcji")
x_zadanie2 = np.linspace(-4,4)
y_zadanie2 = 5*x_zadanie2**2 - 3*x_zadanie2 + 2
plt.plot(x_zadanie2, y_zadanie2, "r")
plt.legend(["5x^2-3x+2"], loc="upper right")

plt.xlabel("x")
plt.xlim(-4,4)

plt.subplot(3, 2, 5)
x2_zadanie2 = np.linspace(-4,4)
y2_zadanie2 = (-2) * (x2_zadanie2 ** 3) + 5
plt.plot(x2_zadanie2, y2_zadanie2, "go", linewidth=5)
plt.legend(["-2x^3+5"], loc="upper center")
plt.title("Drugi wykres")
plt.ylabel("wynik funkcji")
plt.xlabel("x")
plt.xlim(-4,4)
plt.show()

#Zadanie 3.

df_zadanie3 = pd.read_csv("automobile.csv", delimiter=";", nrows=100, header=0)
df2_zadanie3 = df_zadanie3.groupby("Body-style").agg({"Car model": "count"})

plt.pie(df2_zadanie3, textprops={"fontsize": 14}, autopct="%.0f%%")
plt.legend(df2_zadanie3.index)
plt.xlabel("typy samochodów")
plt.title("Rodzaje samochodów")
plt.show()

#Zadanie 4.

df_zadanie4 = pd.read_csv("iris.data")
df_zadanie4 = df_zadanie4[ df_zadanie4["class"] != "Iris-versicolor" ]


sns.scatterplot(data=df_zadanie4, color="red", y="sepal width", x="sepal length")

plt.show()