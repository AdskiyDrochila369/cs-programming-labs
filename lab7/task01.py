numbers = list(map(int, input().split()))

corrected = numbers.copy()

for i in range(len(corrected)):
    if corrected[i] < 0:
        corrected[i] = 0

print(f"Исходные остатки: {numbers}")
print(f"Исправленные остатки: {corrected}")