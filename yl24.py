def upc(code):

    code = str(code)
    code = code.zfill(11)

    check_digit = 0

    for i in range(0, 11, 2):
        check_digit += int(code[i])

    check_digit *= 3

    for i in range(1, 10, 2):
        check_digit += int(code[i])

    check_digit %= 10

    if check_digit != 0:
        check_digit = 10 - check_digit

    return check_digit

print(upc(3600029145))
print(upc(360002914))
print(upc(3600029))