n1 = int(input('sisesta esimene arv: '))
n2 = int(input('sisesta teine arv: '))
n3 = int(input('sisesta kolmas arv: '))

if n1 > n2 and n1 > n3:
    print(n1, 'on maksimum')

elif n2 > n3:
    print(n2, 'on maksimum')

else:
    print(n3, 'on maksimum')