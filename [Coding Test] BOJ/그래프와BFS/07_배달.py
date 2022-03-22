# https://www.acmicpc.net/problem/1175

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())

d = [[[[-1] * 4 for _ in range(4)]for _ in range(m)] for _ in range(n)]

ans = -1
moves = [(-1,0),(1,0),(0,-1),(0,1)]

from collections import deque
q = deque()

ans = -1
r1, c1, r2, c2 = -1, -1, -1, -1
for r in range(n):
    for c in range(m):
        if data[r][c] == 'S':
            for k in range(4):
                q.append((r,c,k,0))
                d[r][c][k][0] = 0
        elif data[r][c] == 'C':
            if r1 == -1:
                r1, c1 = r, c
            else:
                r2, c2 = r, c

while q:
    r, c, direction, s = q.popleft()
    if s == 3:
        ans = d[r][c][direction][s]
        break
    for i in range(4):
        # 연속으로 같은 방향이면 제외
        if i == direction:
            continue
        nr, nc = r + moves[i][0], c + moves[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if data[nr][nc] != '#':
                ns = s
                if data[nr][nc] == 'C':
                    if nr == r1 and nc == c1:
                        ns |= 1
                    else:
                        ns |= 2

# |= : bitwise 연산
# 십진수:이진수
# 0:0, 1:1, 2:10, 3:11
# 따라서 C를 두 번 모두 지나친 경우만 3:11 이 된다 

                if d[nr][nc][i][ns] == -1:
                    d[nr][nc][i][ns] = d[nr][nc][i][s] + 1
                    q.append((nr, nc, i, ns))