a = 2
b = 3
c = 4
'''
def is1000(a, b, c):
    if ((a + b + c) == 1000):
        return 1
    else:
        return 0

def pyThag(a, b, c):
    if ((a**2 + b**2) == c**2):
        return 1
    else:
        return 0

while (a < 999):
    b = (a + 1)
    while (b < 999):
        c = (b + 1)
        while (c < 999):
            print("a - ", a, " b - ", b, " c - ", c, "")
            if (is1000(a, b, c) and pyThag(a, b, c)):
                print(a * b * c)
                exit()
            c += 1
        b += 1
    a += 1
'''
# Slow
while (a < 999):
    b = (a + 1)
    while (b < 999):
        c = (1000 - a - b)
        if (c**2 == (a**2 + b**2)):
            print("a - ", a, " b - ", b, " c - ", c, "")
            print(a * b * c)
        b += 1
    a += 1
# Fast
