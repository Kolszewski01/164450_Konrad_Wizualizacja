import math

z="Zadanie"

print(z," 1\n")
a = 6
b = 9
c = 2.2
d = 9.2
e = "Kasza"
f = "Jaglana"
g = 4j
h = 1+5.3j
print(a, b)
print(c,d)
print(e+" "+f)
print(g, h)
del a,b,c,d,e,f,g,h

print(z," 2\n")

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę  b: "))
print("1.Dodawanie\n 2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n 5.Potęgownie\n")
c = int(input())
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
   print(a*b)
elif c == 4:
    print(a/b)
elif c == 5:
    print(pow(a, b))
else:
    print("NIE DZIALA POPSULO SIE NOWE WIEDO")
del a, b, c

print(z," 3\n")

a = 1
a -= 1
print(a)
b = 1
b += 1
print(b)
c = 2
c /= 2
print(c)
d = 2
d *=2
print(d)
e = 12
e %= 3
print(e)
f = 2
f **= 5
print(f)
del a, b, c, d, e, f

print(z," 4\n")

print(math.e**10)
print(pow(math.log(5+(math.sin(8))**2,math.e),1/6))
print(math.floor(3.55))
print(math.ceil(4.80))

print(z," 5\n")

I = "PATRICK"
N = "SWAYZE"
print(I.capitalize(),N.capitalize())

print(z," 6\n")

la = "la la la"
print(la.count("la"))

print(z," 7\n")

xd = "KonradOKEOKE"
print(xd[1])
print(xd[-1])

print(z," 8\n")

print(la.split(" "))

print(z," 9\n")

string = "CHWALA UKRAINIE"
float =  6.9
hex = hex(16)
print('{0:s} {1:f} {2:s}'.format(string, float, hex))

