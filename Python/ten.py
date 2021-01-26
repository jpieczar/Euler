import math

num = 2
total = 0

def if_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return 0
    return 1

while (num < 2000000):
    if (if_prime(num)):
        print(num)
        total += num
    num += 1
print(total)
