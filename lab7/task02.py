numbers = list(map(int, input().split()))

squares = [n**2 for n in numbers if n > 0 and n % 2 != 0]

print(f"Квадраты: {squares}")