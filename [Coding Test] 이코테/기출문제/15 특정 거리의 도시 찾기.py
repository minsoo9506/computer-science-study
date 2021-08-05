n, m, k, x = 4, 4, 1, 1
graph = [[],
         [2,3],
         [3,4],
         [],
         []]

# "모든 도로의 거리가 1" 이라는 조건 덕분에 BFS를 이용하여 간단히 해결
# 출발점으로 가까이 있는게 최단거리니까

from collections import deque

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append([next_node])

check = False
for i in range(distance):
    if i == k:
        print(i)
        check = True

if not check:
    print(-1)