import heapq
INF = int(1e9)
# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # 여기서 b : 연결된 노드, c : weight

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단거리 꺼내기
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
