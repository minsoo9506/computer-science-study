# https://www.acmicpc.net/problem/14263

w, h = map(int, input().split())
a = [input().strip() for _ in range(w)]

import heapq
group_to_col = [0] * 100
col_to_group = [-1] * 256

def tsort(g):
    # 위상정렬
    n = len(g)
    indeg = [0] * n
    for i in range(n):
        for j in range(n):
            if g[j][i]: # 여기서 순서 주의!
                indeg[i] += 1

    ans = ''
    
    q = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(q, group_to_col[i])

    while q:
        ch = heapq.heappop(q)
        ans += ch
        x = col_to_group[ord(ch)]
        for y in range(n):
            if g[x][y]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    heapq.heappush(q, group_to_col[y])
    
    if len(ans) != n:
        return '-1'
    return ans

n = 0
for i in range(w):
    for j in range(h):
        ch = a[i][j]
        if ch != '.':
            if col_to_group[ord(ch)] == -1:
                col_to_group[ord(ch)] = n
                group_to_col[n] = ch
                n += 1

g = [[False] * n for _ in range(n)]

for k in range(n):
    minx = w - 1
    maxx = 0
    miny = h - 1
    maxy = 0
    for i in range(w):
        for j in range(h):
            if a[i][j] == group_to_col[k]:
                minx = min(minx, i)
                maxx = max(maxx, i)
                miny = min(miny, j)
                maxy = max(maxy, j)
    for i in range(minx, maxx + 1):
        for j in range(miny, maxy + 1):
            if a[i][j] != group_to_col[k]: # 해당 색이 다르면
                g[k][col_to_group[ord(a[i][j])]] = True
                # 현재 색을 먼저 놓고서 다른 색을 놓아야 함
                # k: 현재

ans = tsort(g)
print(ans)