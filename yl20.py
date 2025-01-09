# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
#	8 x 1 = 8
#	8 x 2 = 16
#	…
#	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

print("See programm annab sulle sinu valitud arvuga korrutustabeli.")
arv = int(input("Sisesta enda arv: "))

for i in range(13):
    print(f"{arv} x {i} = {arv * i}")