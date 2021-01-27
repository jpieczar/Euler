from itertools import accumulate, count
from math import sqrt

def count_factors(num):
    sum_ = 2 * sum(num % i == 0 for i in range(1, int(sqrt(num)) + 1))
    return sum_

def triangular_numbers():
    yield from accumulate(count())
    
def main():
    for triangle_nr in triangular_numbers():
        if count_factors(triangle_nr) > 500:
            return triangle_nr

if __name__ == "__main__":
    answer = main()
    if answer:
        print(answer)