# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
#(sõne kui list, mitmemõõtmeline ilist - multi dimensional)

lemmikloom =  input("Sisesta enda lemmikloom: ")

loomaessa = print("Sinu lemmiklooma esimene taht on", lemmikloom[0])

loomataht = lemmikloom[0]

loomalist = ["kass", "koer", lemmikloom]

viimaneelement = loomalist[-1]

viimanetaht = viimaneelement[-1]

print(loomalist)
print("Listi viimase elemendi viimane taht on:", viimanetaht)