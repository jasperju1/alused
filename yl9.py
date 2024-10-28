# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)
import math

x = float(input("Sisesta esimese külje pikkus: "))
y = float(input("Sisesta teise külje pikkus: "))
z = float(input("Sisesta kolmanda külje pikkus: "))

if (x+y>z) or (x+z>y) or (z+y>x):
    print("Kolmnurk eksisteerib.")

elif (x+y<z) or (x+z<y) or (z+y<x):
    print("Kolmnurk ei eksisteeri.")

if (x==y==z):
    print("Kolmnurk on võrdkülgne.")

elif (x==y!=z) or (x==z!=y) or (x!=y==z):
    print("Kolmnurk on võrdhaarne. ")

elif (x!=y!=z):
    print("Kolmnurk on erikülgne.")




