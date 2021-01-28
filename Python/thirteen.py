
str_arr = [line.rstrip('\n') for line in open('13resources.txt')]
num_arr = [int(number) for number in str_arr if number != ""]
total = sum(num_arr)

print("First 10 significant digits = {}".format(str(total)[:10]))