import random
import geometryczny
import arytmetyczny
#  1 Zadanie
#
#  #
#
#  a=[]
#
#  a=[1-x for x in range(11)]
#
#  print(a)
#
#  b=[]
#
#  b=[4**x for x in range(7)]
#
#  print(b)
#
#  c=[]
#
#  c=[x for x in b if x % 2 == 0]
#
#  print(c)
#
# Zadanie 2
#  lista1=[]
#
#  for x in range(10):
#      lista1.append(random.randint(0,100))
#
#  lista2=[x for x in lista1 if x%2==0]
#
#  print(lista2)
#
# Zadanie 3
#
#  xd="sztuki"
#  l3={"Pomidor":"kg","Cola":"sztuki","ziemniaki":"kg","marchew":"sztuki"}
#
#  l4={value: value for xd,value in   l3.items()}
#
#  print(l4)
#
# Zadanie 4
#
#  a=int(input("podaj a: "))
#  b=int(input("podaj b: "))
#  c=int(input("podaj przekatna: "))
#
#  def trojkat(a,b,c):
#      if a ** 2 + b ** 2 == c ** 2:
#          print("tak jest prostokatny")
#      else:
#          print("nie jest prostokatny")
#
# trojkat(a,b,c)
#
# Zadanie 5
#
#  def trapez(a=0,b=0,h=0):
#      p=((a+b)*h)/2
#      print(p)
#
#
#  trapez()
#
# Zadanie 6
#
#  def ciag(a=1,b=4,ile=10):
#      c=a
#      lista=[]
#      for a in range(ile):
#          c=c*b
#          lista.append(c)
#      d=1
#      for x in lista:
#          d=d*x
#
#      print(d)
#
#  ciag()
#
#  #Zadanie 7
#
#  def ciag2(*ciag):
#      if len(ciag)==0:
#          return 0
#      else:
#          il=1
#          for x in ciag:
#              il *= x
#          return il
#
# print(ciag2(1,4,10))
#
# Zadanie 8
#
# def zakupy(** lista):
#     l=0
#     pln=0
#     listapln=[]
#     for x in lista:
#         l+=1
#     for x in lista:
#         pln= pln+lista[x]
#         # listapln.append(lista[x])
#
#     print("ilosc produktów: " + str(l))
#     print("Cena za wszystkie produkty: " + str(pln))
#
# print(zakupy(chleb=7,ser_topiony=3,Losos_wedzony=10,hehe=69))
#

#9 Zadanie

print(geometryczny.geo_ogolny(1,3,4))
print(arytmetyczny.aryt_suma(1,3,4))
