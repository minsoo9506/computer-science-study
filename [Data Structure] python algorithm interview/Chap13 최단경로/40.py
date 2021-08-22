# 네트워크 딜레이 타임
N = 4
k = 2
times = [[2,2,1],[2,3,1],[3,4,1]] # 출발지, 도착지, 소요시간

import collections
import heapq

def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Q 변수 : [(해당 도착점까지 소요시간, 도착점)]
    Q = [(0, k)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q) # 소요시간이 적은 것부터 pop
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                tmp = time + w
                heapq.heappush(Q, (tmp, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1


# 내 풀이
n = 4
k = 2
times = [[2,1,1],
         [2,3,1],
         [3,4,1]]

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