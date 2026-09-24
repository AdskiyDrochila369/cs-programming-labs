second = int(input())

hourse = second // 3600
minute = (second % 3600) // 60
second = second % 60
print(f"{hourse:02d}:{minute:02d}:{second:02d}")