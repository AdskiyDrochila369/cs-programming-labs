elements = list(map(int, input().split()))   
number = int(input())

indexed = [index for index, element in enumerate(elements) if element == number]

print(f"Индексы: {indexed}")
