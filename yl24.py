#UPC vöötkoodi kontrollsumma arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri kontrollsumma arvutamise funktsioon. (https://www.w3schools.com/python/python_functions.asp)

def upc(code):
    code = str(code)

    code = code.zfill(11)

    for el in range(0, 12, 2):
        print(code[i])

    print(code)


upc(3600029145)
upc(360002914)
upc(3600029)