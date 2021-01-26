a = 2
b = 3
c = 4
while (a < 999):
    b = (a + 1)
    while (b < 999):
        c = (1000 - a - b)
        if (c**2 == (a**2 + b**2)):
            print("a - ", a, " b - ", b, " c - ", c, "")
            print(a * b * c)
        b += 1
    a += 1
