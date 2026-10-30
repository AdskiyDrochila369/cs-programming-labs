n = int(input())

odd_count = 0

for r in range(n):
    number = 1
    row = ""

    for k in range(r + 1):
        if k > 0:
            row += " "

        row += str(number)

        if number % 2 != 0:
            odd_count += 1

        if k < r:
            number = number * (r - k) // (k + 1)

    print(row)

print(f"Нечетных элементов: {odd_count}")