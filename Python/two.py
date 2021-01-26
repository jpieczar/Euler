a = 1
b = 2
c = 0
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    c = a
    a = b
    b += c
print(total)

