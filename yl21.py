# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

from random import randint

number = randint(1, 100)
print(number)

while True:
    pakkumine = int(input("Paku mis arvu arvuti välja mõtles: "))

    if pakkumine == number:
        print("Pakkusid arvu õigesti!")
        break

    elif pakkumine > number:
        print("Sinu arv on liiga suur, paku uuesti: ")

    elif pakkumine < number:
        print("Sinu arv on liiga väike, paku uuesti: ")
