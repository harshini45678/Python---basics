numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [0]
]

print(numbers[0][2])
print(numbers[2][1])
print(numbers[4][0])

for row in numbers:
    for col in row:
        print(col, end = " ")