# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9.
# Arvuta n + nn + nnn väärtus ja väljasta see.
# (Näiteks kui kasutaja sisestab 2,
# siis on vaja väljastada tulemus 2 +     22 + 222 = 246).
# Ära kasuta korrutamistehet.
# Ülesanne on lahendatav ainult liitmise operaatorit kasuades. 

n = input('1-9: ')
nn = n + n 
nnn = n + n + n
result= int(n) + int(nn) + int(nnn)

print(n, '+', nn, '+', nnn, '=', result)
