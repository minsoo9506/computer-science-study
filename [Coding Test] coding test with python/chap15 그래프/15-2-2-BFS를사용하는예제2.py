# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

from collections import deque
q = deque()
q.append((0,0,0))
moves = [(-1,0),(1,0),(0,-1),(0,1)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1
while q:
    r, c, wall = q.popleft()
    if r == n - 1 and c == m - 1:
        print(visit[r][c][wall])
        break
    for i in range(4):
        nr, nc = r + moves[i][0], c + moves[i][1]
        if 0 <= nr < n and 0 <= nc < m and visit[nr][nc][wall] == 0:
            if data[nr][nc] == 0:
                visit[nr][nc][wall] = visit[r][c][wall] + 1
                q.append((nr, nc, wall))
            if data[nr][nc] == 1 and wall == 0:
                visit[nr][nc][1] = visit[r][c][0] + 1
                q.append((nr, nc, 1))