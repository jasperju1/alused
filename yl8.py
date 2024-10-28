# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

print("See programm kontrollib, kas aasta on liig- või lihtaasta.")
n1 = int(input ("Sisesta aastaarv: "))

if (n1 % 400==0):
    print("Arv on liigaasta")

elif (n1 % 4==0) and (n1 % 100!=0):
    print("Arv on liigaasta")

elif (n1 % 400!=0):
    print("Arv on lihtaasta")

