sum_square = 0
for i in range(1, 101):
    sum_square += i**2
print(sum_square)

square_sum = 0
for i in range(1, 101):
    square_sum += i
print(square_sum**2)

print(square_sum**2 - sum_square)
