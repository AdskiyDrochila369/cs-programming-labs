price = float(input())
age = int(input())

if price < 0 or 120 < age < 0:
    print("Ошибка")
elif age <= 5:
    cost = 0
elif age <= 17:
    cost = price * 0.5
elif age <= 59:
    cost = price
else:
    cost = price * 0.7

print(f"Стоимость: {cost:.2f} руб")
