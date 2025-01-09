# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv.

tekst = input("Sisesta siia oma tekst: ")

täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"

täishäälikute_arv = 0

for tähemik in tekst:
    if tähemik in täishäälikud:
        täishäälikute_arv += 1

print("Täishäälikute arv tekstis on:", täishäälikute_arv)
