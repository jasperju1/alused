I = 1
II = 2
III = 3
IV = 4
V = 5
VI = 6
VII = 7
VIII = 8
IX = 9
X = 10

a = 2230
r = a * I
print(r)
print(315 // 100)

m = a // 1000
d = (a-m * 1000) // 100
x = (a-d * 100 - m * 1000) // 10
i = (a-x * 10 - d * 100 - m * 1000) // 1
if m == 0:
    print(d,x,i)
else:
    print(m,d,x,i)