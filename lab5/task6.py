n = int(input())

odd_count = 0

for row in range(n):
    coefficient = 1
    line = ""

    for column in range(row + 1):
        if column > 0:
            line += " "

        line += str(coefficient)

        if coefficient % 2 != 0:
            odd_count += 1

        if column < row:
            coefficient = coefficient * (row - column) // (column + 1)

    print(line)

print(f"Нечетных элементов: {odd_count}")