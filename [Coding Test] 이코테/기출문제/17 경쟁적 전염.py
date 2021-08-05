n = 3
k = 3
data = [[1,0,2],
        [0,0,0],
        [3,0,0]]

target_s = 2
target_row = 3
target_col = 2

dr = [0,-1,0,1]
dc = [1,0,-1,0]

x = []

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            x.append((data[i][j], 0, i, j))

# 정렬한 후에 queue에 넣기
# virus의 숫자가 낮을수록 우선순위
x.sort()
from collections import deque
q = deque(x)

while q:
    virus, s, r, c = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if data[nr][nc] == 0:
                data[nr][nc] = virus
                q.append((virus, s + 1, nr, nc))

print(data[target_row - 1][target_col - 1])