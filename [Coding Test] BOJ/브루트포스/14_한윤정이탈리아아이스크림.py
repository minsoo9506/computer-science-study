# https://www.acmicpc.net/problem/2422

n, m = 5, 3
data = [[0] * 201 for _ in range(201)]
for _ in range(m):
    x = list(map(int, input().split()))
    data[x[0]][x[1]] = 1
    data[x[1]][x[0]] = 1

from itertools import combinations
result = 0
candidates = combinations(range(1, n + 1), 3)
for c in candidates:
    if data[c[0]][c[1]] + data[c[1]][c[2]] + data[c[0]][c[2]] == 0: 
        result += 1

print(result)