n = 3
# [출발, 도착, 가격]
edges = [[0,1,100],[1,2,100],[0,2,500]]
# 출발
src = 0
# 도착지
dst = 2
# 거치는 node 수
k = 0

import collections
import heapq

dist = [int(1e9)] * n

def find(flights, src, K):
    graph = collections.defaultdict(list)
    for u, v, w, in flights:
        graph[u].append((v, w))

    # Q : [(가격, 도착점, 남은 경유지 수)]
    Q = []
    heapq.heappush(Q, (0, src, K))
    while Q:
        price, node, k = heapq.heappop(Q)
        if dist[node] < price:
            continue
        if k >= 0:
            for v, w in graph[node]:
                tmp = price + w
                if tmp < dist[v]:
                    dist[v] = tmp
                    heapq.heappush(Q, (tmp, v, k-1))

find(edges, src, k)
print(dist[dst])
print(dist)