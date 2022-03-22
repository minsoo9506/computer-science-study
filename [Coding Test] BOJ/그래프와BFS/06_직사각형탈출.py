# https://www.acmicpc.net/problem/16973
# 부분합을 이용

n, m = map(int, input().split())
data = [[0] * (m + 1) for _ in range(n + 1)]
s = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    data[i][1:] = list(map(int, input().split()))
h, w, sr, sc, fr, fc = map(int, input().split())

from  collections import deque

# (부분합이용) 해당 직사각형을 움직였을 때, 1을 침범했는지 확인
def check(r, c, er, ec):
    return s[er][ec] - s[er - 1][ec] + s[er][ec - 1] + s[er][ec]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + data[i][j]

q = deque()
q.append((sr, sc)) # 시작위치

dist = [[-1] * (m + 1) for _ in range(n + 1)]
dist[sr][sc] = 0

moves = [(0,1),(0,-1),(1,0),(-1,0)]

while q:
    r, c = q.popleft()
    for move in moves:
        nr = r + move[0]
        nc = c + move[1]
        if 1 <= nr \
            and 1 <= nc \
            and nr + h - 1 <= n \
            and nc + w - 1 <= m \
            and check(nr, nc, nr + h - 1, nr + w - 1) == 0 \
            and dist[nr][nc] == -1:
            dist[nr][nc] += dist[r][c] + 1
            q.append((nr, nc))

print(dist[fr][fc])