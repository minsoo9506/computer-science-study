# https://www.acmicpc.net/problem/14502
# 연구소

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

virus = []
empty = []
for r in range(n):
    for c in range(m):
        if data[r][c] == 2:
            virus.append((r, c))
        if data[r][c] == 0:
            empty.append((r,c))

from itertools import combinations
candidates = combinations(empty, 3)

from collections import deque
moves = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs_virus(r, c, check):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + moves[i][0], c + moves[i][1]
            if 0 <= nr < n and 0 <= nc < m and check[nr][nc] == 0:
                check[nr][nc] == 2
                q.append((nr, nc))

def get_result(check):
    result = 0
    for r in range(n):
        for c in range(m):
            if check[r][c] == 0:
                result += 1
    return result                 

import copy
check = copy.deepcopy(data)
result = 0

for candidate in candidates:
    # 벽세우고
    for r, c in candidate:
        check[r][c] = 1
    # 바이러스
    for r, c in virus:
        bfs_virus(r, c, check)
    # 결과
    tmp_result = get_result(check)
    result = max(result, tmp_result)
    # 다시 리셋
    for r in range(n):
        for c in range(m):
            check[r][c] = data[r][c]