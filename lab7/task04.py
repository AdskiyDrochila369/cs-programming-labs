
n, m = map(int, input().split())
    
table = [(list(map(int, input().split())))[:m] 
             for _ in range(n)]

rows_sum = [sum(row) for row in table]
columns_sum = \
        [sum(table[i][j] for i in range(n)) for j in range(m)]

print(f'Суммы строк: {rows_sum}')
print(f'Суммы столбцов: {columns_sum}')