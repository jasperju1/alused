# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta

mylist = ["watermelon", "strawberry", "apelsiin"]
print(mylist[0])

mylist.append("mango")
print(mylist[3])

mylist[1] = "banana"
print(mylist)

if "apple" in mylist:
    print("apple exists")

else:
    print("apple doesn't exist")

print(len(mylist))

mylist.remove("mango")
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)