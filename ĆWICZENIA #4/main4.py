import sys

# class Ksztalty:
#     __xd__="xyz"
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#         self.opis = "To będzie klasa dla ogólnych kształtów"
#     def pole(self):
#         return self.x * self.y
#     def obwod(self):
#         return 2* self.x + 2* self.y
#     def dodaj_opis(self, text):
#         self.opis=text
#     def skalowanie(self,czynnik):
#         self.x=self.x * czynnik
#         self.y=self.y * czynnik
#
# prostokat=Ksztalty(10,30)
#
# print(prostokat.pole())
# print(prostokat.obwod())
# prostokat.dodaj_opis("Prostokat")
# print(prostokat.opis)
# prostokat.skalowanie(0.5)
# print(prostokat.x)
#
# prostokat.__xd__="nana"
# print(prostokat.__xd__)
#
#

#ZADANIE 1

# lista=[]
#
# for x in range(31):
#     lista.append(x)
#
# with open("plik.txt","w+") as plik:
#     for x in lista:
#         lista[x]=x*2
#     plik.writelines(str(lista))

#ZADANIE 2

# plik=open("plik.txt","r")
# wiersze=plik.readlines()
#
# print(wiersze)
# plik.close()

#ZADANIE 3

# tekscior=""""Gdzieś daleko i bardzo wysoko
# Gdzie zwykły śmiertelnik nie stąpa tam nogą
# Gdzie spokój, harmonia i natury zew
# Gdzie słychać szum drzew i ptaków śpiew
# Wschód słońca pada na twarz
# Wypełnia twą duszę, którą ciągle masz
# Wydaje się tobie że te uczucie już znasz, ale
# Ono wcale nie jest ci znane
# Chociaż było pisane i pisane też jest nam
# Tak że wszyscy się spotkamy, więc nie będziesz już sam
# Spotkasz ludzi których tak bardzo kochałeś
# Choć lata nie widziałeś nadal kochać nie przestałeś (Yo!)
# """
#
# with open("plik.txt","w+") as plik:
#     plik.writelines(tekscior)
#
# with open("plik.txt", "r+") as plik:
#     for x in plik:
#         print(x, end="")
#

# ZADANIE 4

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("Nazwa: "+ self.nazwa_produktu)
#         print("Ilosc: " + str(self.ilosc) + " " + self.jednostka_miary)
#         print("Cena: " + self.jednostka_miary + ": " + str(self.cena_jed) + " PLN")
#
#     def ile_produktu(self):
#         print(str(self.ilosc) +" "+ self.jednostka_miary)
#
#     def ile_kosztuje(self, ile):
#         return self.cena_jed * ile
#
# Ziemniaki = NaZakupy("ziemniaki", 3, "kg", 2)
#
# Ziemniaki.wyswietl_produkt()
#
# Ziemniaki.ile_produktu()
#
# print(Ziemniaki.ile_kosztuje(3))
#


# ZADANIE 5

class Ciagi_Arytmetyczne:

    def __init__(self, n1, r, n):
        self.n1 = n1
        self.r = r
        self.n = n
        self.all = [n1+r*(x-1) for x in range(1, n+1)]

    def wyswietl_dane(self):
        print(self.all)

    def pobierz_elementy(self, *all):
        self.all = [x for x in all]

    def pobierz_parametry(self, n1, r, n):
        self.n1 = n1
        self.r = r
        self.n = n
        self.all = [self.n1 + self.r * (x - 1) for x in range(1, self.n + 1)]

    def policz_sume(self):
        return sum(self.all)

    def policz_elementy(self):
        return ((self.all[-1]-self.n1)/self.r)+1


np = Ciagi_Arytmetyczne(3, 4, 1)

np.wyswietl_dane()

np.pobierz_elementy(55, 2, 30)

np.wyswietl_dane()

np.pobierz_parametry(6, 2, 3)

np.wyswietl_dane()

print(np.policz_sume())

print(np.policz_elementy())

