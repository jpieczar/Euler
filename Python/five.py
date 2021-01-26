def no_rem(num):
    for i in range(2, 21):
        if num % i != 0:
            return 0
    return 1

i = 200000000
while (True):
    if no_rem(i):
        print(">>>", i)
        exit()
    i += 1
#232792560
