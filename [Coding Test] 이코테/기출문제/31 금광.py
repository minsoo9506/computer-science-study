n, m = 3, 4
data = [[1,3,3,2],
        [2,1,4,1],
        [0,6,4,7]]

for row in range(n):
    for col in range(1, m):
        if row == 0:
            data[row][col] += max(data[row][col - 1], data[row + 1][col - 1])
        elif row == n - 1:
            data[row][col] += max(data[row][col - 1], data[row - 1][col - 1])
        else:
            data[row][col] += max(data[row][col - 1], data[row - 1][col - 1], data[row + 1][col - 1])

result = 0
for i in range(m):
    result = max(result, data[n - 1][i])
print(result)