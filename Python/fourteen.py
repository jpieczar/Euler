def collatz(number):

    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

def longest_sequence():
    
    longest = 0
    longest_num = 0
    for i in range(1, 1000000):
        number = i
        seq = 1
        while number != 1:
            number = collatz(number)
            seq += True
            if seq > longest:
                longest = seq
                longest_num = i
    return longest, longest_num
    
longest_seq, init = longest_sequence()

print("Longest Collatz sequence with starting int within range(0, 1M) = {}".format(longest_seq))
print("The initiating number is = {}".format(init))