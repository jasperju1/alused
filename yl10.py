nimi = input("Sisesta enda nimi: ")

greeting = input(f"Tere, {nimi}, kuidas teil läheb? ")

elukoht = input("Sisesta enda elukoht: ")

if (elukoht=="saaremaa") or (elukoht=="Saaremaa"):
    saarlane = input("Mina elan ka saaremaal!")

vanus = int(input ("Sisestage enda vanus: "))

if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")

elif vanus == 18:
    print("Palju õnne täisealiseks saamise puhul!")

elif vanus > 18:
    print("Sa võid autot juhtida.")

else: 
    vanus = int(input ("Sisestage enda vanus: "))
