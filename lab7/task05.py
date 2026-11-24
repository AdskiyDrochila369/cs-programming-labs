r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]

row_start, row_end, column_start, column_end = map(int, input().split())
target = int(input())

found = False
for i in range(row_start, row_end + 1):
    for j in range(column_start, column_end + 1):
        if table[i][j] == target:
            print(i, j)
            found = True

if not found:
    print("Не найдено")