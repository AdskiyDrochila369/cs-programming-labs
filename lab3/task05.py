pit = input()

print(f"Длина: {len(pit)}")
print(f"Только буквы: {pit.isalpha()}")
print(f"Только цифры: {pit.isdigit()}")
print(f"Буквенно-цифровая: {pit.isalnum()}")
print(f"Содержит дефис: {'-' in pit}")


