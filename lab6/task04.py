n = int(input())

if n < 0:
    print("Ошибка")
else:
    count = 0
    total = 0

    while (n % 10 != n):
        count += 1
        total += n % 10 
        n //= 10

    count += 1
    total += n

    print("Цифр:", count)
    print("Сумма цифр:", total)