def is_palindrome(num):
    b = []
    string = ""
    hold = num
    while num >= 10:
        b.append(num % 10)
        num //= 10
    if num < 10:
        b.append(num)
    for i in b:
        string += str(i)
    if hold == int(string):
        return 1
    return 0

hold = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            print("i: ", i, " j: ", j)
            print("i * j -> ", i * j)
            if (i * j) >= hold:
                hold = (i * j)
print("END ", hold)
