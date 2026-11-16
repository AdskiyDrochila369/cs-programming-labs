n = int(input())

if n < 2:
    print("Ошибка")
else:
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    print(*factors)