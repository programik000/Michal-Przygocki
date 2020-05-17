import math
a=float(input("Podaj liczbe a:"))
b=float(input("Podaj liczbe b:"))
c=float(input("Podaj liczbe c:"))
 
if a==0:
    print("Równanie liniowe ")
    if b!=0:
        print("Jeden pierwiatek")
        x=-c/b
        print("x = {0}".format(x))
    elif c!=0:
        print("Brak rozwiazania")
    elif c==0:
        print("Równanie ma nieskonczenie wiele rozwiazan")                       
else:
    print("Równanie  kwadratowe")
    d=b*b-4*a*c
    if d<0:
        print("Brak rozwiązań")
    elif d==0:
        print("Jeden pierwiastek podwojny")
        x=-b/(2*a)
        print("x = {0}".format(x))
    elif d>0:
        print("Dwa pierwiastki ")
        from math import sqrt
        x1=(-b-sqrt(d))/(2*a)
        x2=(-b+sqrt(d))/(2*a)
        print("x1 = {0}, x2 = {1}".format(x1,x2))
