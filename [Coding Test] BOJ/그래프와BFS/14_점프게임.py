# https://www.acmicpc.net/problem/15558

n, k = map(int, input().split())
data = [list(input()) for _ in range(2)]

# 1초마다 사라지는거 고려 
# -> 해당 칸으로의 최단거리(시간)를 구한 뒤, 그 최단거리(시간)와 위치값을 비교
# -> nc < dist[r][c] + 1: 이러면 사라진 상태라 못 감

from collections import deque

moves = [(0,1),(0,-1),(1,k)]
q = deque([])
q.append((0, 0))
dist = [[-1] * n for _ in range(2)]
dist[0][0] = 0
ok = False

while q:
    r, c = q.popleft()
    for i in range(3):
        nr, nc = r + (moves[i][0] + 1) % 2, c + moves[i][1]
        if nc >= n:
            ok = True
            break
        if data[nr][nc] == 1 and dist[nr][nc] == -1 \
            and nc >= 0 and nc >= dist[r][c] + 1:
            dist[nr][nc] = dist[n][c] + 1
            q.append((nr, nc))
    if ok:
        break

if ok:
    print(1)
else:
    print(0)