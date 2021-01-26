import math
'''
def if_prime(num):
    #for i in range(2, num):
        if num % i == 0:
            return 0#
    if (math.sqrt(num).is_integer()):
        return 0
    return 1'''

def if_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return 0
    return 1

hold_me = 0
for i in range(2, 6858):
    if if_prime(i):
        if 600851475143 % i == 0:
            hold_me = i
            #print(i)
print(hold_me)
# This takes a while to run in Python3 ...
