n = 3

graph = [[5,5,4],
         [3,9,1],
         [3,2,7]]

INF = int(1e9)
distance = [[INF] * n for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = 0, 0
distance[r][c] = graph[r][c]

import heapq

q = [(graph[r][c], r, c)]

while q:
    dist, r, c = heapq.heappop(q)
    if distance[r][c] < dist:
        continue
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        cost = dist + graph[nr][nc]
        if cost < distance[nr][nc]:
            distance[nr][nc] = cost
            heapq.heappush(q, (cost, nr, nc))

print(distance[r - 1][c - 1])