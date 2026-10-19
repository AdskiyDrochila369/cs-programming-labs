years = int(input())

if not 1 <= years <= 9999:
    print("Ошибка")
elif years % 400 == 0 or (years % 4 == 0 and years % 100 != 0):
    print("Високосный")
else:
    print("Невисокосный")
