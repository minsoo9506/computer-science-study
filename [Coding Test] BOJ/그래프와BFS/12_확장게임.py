# https://www.acmicpc.net/problem/16920

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
data = [[0] for _ in range(n)]
for i in range(n):
    data[i] = list(input().split())


from collections import deque

q = []
for r in range(n):
    for c in range(m):
        if data[r][c] != '.':
            q.append((r, c, data[r][c]))

q = sorted(q, key=lambda x: x[2])
q = deque(q)

moves = [(-1,0),(1,0),(0,-1),(0,1)]

while q:
    r, c, d = q.popleft()
    for i in range(1, s[int(d) - 1] + 1):
        for j in range(4):
            nr, nc = r + i * moves[j][0], c + i * moves[j][1]
            if 0 <= nr < n and 0 <= nc < m and data[nr][nc] == '.':
                data[nr][nc] = d
                q.append((nr, nc, d))


for i in range(1, p + 1):
    result = 0
    for r in range(n):
        for c in range(m):
            if data[r][c] == str(i):
                result += 1
    print(result, end=' ')
print(data)