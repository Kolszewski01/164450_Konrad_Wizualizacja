# a=int(input("podaj a:"))
# b=int(input("podaj b:"))
# if a==b:
#     print("rowne")
# else:
#     print("nierowne")
#
# a=int(input("podaj a:"))
# b=int(input("podaj b:"))

# if a>b:
#     print("liczba a jest wieksza od b")
# elif a<b:
#     print("b jest wieksza od a")
# else:
#     print("liczby są rowne")
#

# a=input("podaj b:")
# print(a)
# print(type(a))

# a=int(a)
# print(type(a))
#
# a=input("wpisz 1 liczbe: ")
# b=input("wpisz 2 liczbe: ")
# c=input("wpisz 3 liczbe: ")
# d=input("wpisz 4 liczbe: ")
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
#
# if (a>b)&(c>d):
#     print('liczba a jest wieksza od liczby b i c jest wieksza od d')
# else:
#     print("liczba a jest mniejsza od liczby b lub c jest mniejsze od d")
#

# for i in range(0, 7, 1):
#     print(i)

# lista=['a',5,6,5.6]
# for a in lista:
#     print(a)
# else:
#     print('wyswietlone zostaly wszystkie elementy z LISTY')
#


# a=1
# while a<9:
#     print(a)
#     a+=1

# lista=[4,6,9,5,7,2,3]
# liczba=input('podaj liczbe: ')
# licznik=0
# while licznik <len(lista):
#      if int(liczba) - lista[licznik]==0:
#          print('liczba '+ str(liczba)+' - '+str(lista[licznik])+ ' = 0')
#          break
#     else:
#     licznik += 1
# else:
#     print("Żadna z wartosci nie dala odpowiedniego wyniku")
#
#
#
# lista1=[4,6,8,2,3,9]
# lista2=[4,7,5,2]
# suma=[]
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# try:
#
# except nazwa_błędu 1:
#
# a=input("wczytaj 1 liczbe: ")
# b=input("wczytaj 2 liczbe: ")
#
# try:
#     a=int(a)
#     b=int(b)
#     wynik=a/b
#     print(wynik)
#
# except ZeroDivisionError:
#     print("Pamietaj chole*o nie dziel przez 0")
# except ValueError:
#     print("NIE WCZYTANO LICZBY CALKOWITEJ")

lista=['a',5,5.5,[1,2,3],'hg']
słownik={1:40,'a':'b',4:50}

print(słownik[1])

słownik['30k']=[3,0,'k']

print(słownik['30k'])

słownik[1]=słownik[1]-5

print(słownik)

słownik.pop('a')
lista.append('xd')
lista.insert(2, 22)
lista.reverse()
lista.remove('a')
print(lista)
print(lista.index(5))
print(słownik)
print(lista)
