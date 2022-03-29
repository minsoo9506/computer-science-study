# https://www.acmicpc.net/problem/15653

from collections import deque
import copy

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def simulate(a, k, r, c):
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nr, nc = r + moves[k][0], c + moves[k][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return moved, False, r, c
        if a[nr][nc] == '#':
            return moved, False, r, c
        elif a[nr][nc] in 'RB': 
            return moved, False, r, c
        elif a[nr][nc] == '.':
            a[r][c], a[nr][nc] = a[nr][nc], a[r][c]
            r, c = nr, nc
            moved = True
        elif a[nr][nc] == '0':
            a[r][c] = '.'
            moved = True
            return moved, True, r, c

def go(b, r1, c1, r2, c2, direction):
    a = copy.deepcopy(b)
    a[r1][c1] = 'R'
    a[r2][c2] = 'B'
    hole1 = False
    hole2 = False
    while True:
        rmoved, rhole, r1, c1 = simulate(a, direction, r1, c1)
        bmoved, bhole, r1, c1 = simulate(a, direction, r2, c2)
        if not rmoved and not bmoved:
            break
        if rhole:
            hole1 = True
        if bhole:
            hole2 = True
    return hole1, hole2, r1, c1, r2, c2

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
d = [[[[-1] * m for k in range(n)] for j in range(m)] for i in range(n)]
ans = -1

q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            hr, hc = i, j
        elif a[i][j] == 'R':
            r1, c1 = i, j
            a[i][j] = '.'
        elif a[i][j] == 'B':
            r2, c2 = i, j
            a[i][j] = '.'

q.append((r1,c1,r2,c2))
d[r1][c1][r2][c2] = 0
found = False

while q:
    r1, c1, r2, c2 = q.popleft()
    for k in range(4):
        hole1, hole2, nr1, nc1, nr2, nc2 = go(a, r1, c1, r2, c2, k)
        if hole2:
            continue
        if hole1:
            found = True
            ans = d[r1][c1][r2][c2] + 1
            break
        if d[nr1][nc1][nr2][nc2] != -1:
            continue
        q.append((nr1, nc1, nr2, nc2))
        d[nr1][nc1][nr2][nc2] = d[r1][c1][r2][c2] + 1
    if found:
        break
print(ans)