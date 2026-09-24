distance_km = int(input())
fuel_consumption_per_100_km = float(input())
cost_per_liter = float(input())

print(f"Топливо: {distance_km * fuel_consumption_per_100_km / 100:.2f} л")
print(f"Стоимость: {distance_km * fuel_consumption_per_100_km / 100 * cost_per_liter:.2f} руб")
