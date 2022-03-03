# https://www.acmicpc.net/problem/15686

n, m = 5, 3
data = [
    [0,0,1,0,0],
    [0,0,2,0,1],
    [0,1,2,0,0],
    [0,0,1,0,0],
    [0,0,0,0,2]
]

chicken = []
home = []
for r in range(n):
    for c in range(n):
        if data[r][c] == 2:
            chicken.append((r, c))
        if data[r][c] == 1:
            home.append((r, c))

from itertools import combinations

result = int(1e9)
for candidate in list(combinations(chicken, m)):
    min_distance = 0
    for h in home:
        distance = int(1e9)
        for c in candidate:
            distance = min(distance, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        min_distance += distance
    result = min(result, min_distance)
print(result)