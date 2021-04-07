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