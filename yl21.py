# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random

question = "y"

while question == "y":

    number = random.randint(1, 100)
    print(number)

    while True:
        guess = int(input("Paku mis arvu arvuti välja mõtles: "))

        if guess == number:
            print("Pakkusid arvu õigesti!")
            break

        elif guess > number:
            print("Sinu arv on liiga suur.")

        elif guess < number:
            print("Sinu arv on liiga väike.")    

    question = input("Kas sa soovid uuesti mängida? (y/n): ")
