def if_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

count = 0
for i in range(2, 200000000):
    if if_prime(i) and count == 10000:
        print(i)
        exit()
    if if_prime(i):
        count += 1
#104743
