data = input().split(";")

number = data[0]
from_city = data[1]
to_city = data[2]
time = data[3]
price = float(data[4])

print(f"Поезд: {number}")
print(f"Маршрут: {from_city} - {to_city}")
print(f"Отправление: {time}")
print(f"Цена: {price:.2f} руб")