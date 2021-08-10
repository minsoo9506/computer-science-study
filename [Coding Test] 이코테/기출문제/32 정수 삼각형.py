n = 5

data = [[7],
        [3,8],
        [8,1,0],
        [2,7,4,4],
        [4,5,2,6,5]]

for row in range(1, n):
    for col in range(row + 1):
        if col == 0:
            data[row][col] += data[row - 1][0]
        elif col == row:
            data[row][col] += data[row - 1][-1]
        else:
            data[row][col] += max(data[row - 1][col - 1], data[row - 1][col])

result = 0
for i in range(n):
    result = max(result, data[n - 1][i])

print(result)