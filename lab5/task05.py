count = 0
total = 0

while True:
    line = input()

    if line == "stop":
        break

    count += 1
    total += int(line)

if count == 0:
    print("Нет покупок")
else:
    avarage = total / count
    print(f"Покупок: {count}")
    print(f"Общая сумма: {total}")
    print(f"Средняя сумма: {avarage:.2f}")