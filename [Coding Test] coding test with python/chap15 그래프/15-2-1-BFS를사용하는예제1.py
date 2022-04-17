# https://www.acmicpc.net/problem/2178
# 미로탐색

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

q = deque([])
q.append((0,0))
maze[0][0] = 1
moves = [(0,1), (0,-1), (1,0), (-1,0)]

while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + moves[i][0], c + moves[i][1]
        if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1:
            maze[nr][nc] = maze[r][c] + 1
            q.append((nr, nc))

print(maze[n - 1][m - 1])