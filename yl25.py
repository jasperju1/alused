
# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
# Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
# Muuda magustoidu väärtust.
# Tee kordus üle dictionary ja väljasta kõik võtmed.
# Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
# Kontrolli, kas isikukood on dictionary's olemas.
# Leia dictionary suurus (elementide arv).
# Lisa element enda pikkuse jaoks.
# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.


thisdict = { 
      "first_name": "Artur",
      "last_name": "Kass",
      "date_of_birth": "2006",
      "location": "Pärnu",
      "favourite_game": "Angry birds"
}

print(thisdict.get("location"))
print(thisdict["location"])

thisdict["favourite_game"] = "Minecraft"
print(thisdict)

for x in thisdict.keys():
      print(x)

for x in thisdict.values():
      print(x)

if "isikukod" in thisdict:
      print("Yes, 'isikukood' exists") 
else: 
      print("No, 'isikukood' pole") 

print(len(thisdict))

thisdict["height"] = 186
print(thisdict)

thisdict.pop("date_of_birth")
print(thisdict)

thisdict.clear()
print(thisdict)