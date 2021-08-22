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

INF = int(1e9)
dist = [INF] * (n + 1)
dist[0] = 0

def networkDelay(times, n, k):
    global dist
    graph = collections.defaultdict(list)
    for start, end, weight in times:
        graph[start].append((end, weight))

    q = []  
    heapq.heappush(q, (0, k))
    dist[k] = 0
    while q:
        time, node = heapq.heappop(q)
        if dist[node] < time:
            continue
        for end, weight in graph[node]:
            cost = time + weight
            if cost < dist[end]:
                dist[end] = cost
                heapq.heappush(q, (cost, end))

networkDelay(times, n, k)
print(max(dist))
print(dist)