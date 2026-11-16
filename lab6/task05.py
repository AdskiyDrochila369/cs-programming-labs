n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        row = []
        for j in range(n):
            if i > j:
                row.append(i - j)
            else:
                row.append(j - i)
        print(*row)