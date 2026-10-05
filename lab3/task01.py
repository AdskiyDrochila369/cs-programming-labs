document = input()

category = document[:3]
year = document[4:8]
number = document[9:13]

print("Категория:", category)
print("Год:", year)
print("Номер:", number)
print("Обратный номер:", number[::-1])