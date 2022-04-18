# https://www.acmicpc.net/problem/1260
# DFS와 BFS

n, m, v = map(int, input().split())
data = [[] * n for _ in range(n)]
for _ in range(m):
    start, end = map(int, input().split())
    data[start].append(end)

visit = [[0] * n]
dfs_result = []
def dfs(node):
    visit[node] = 1
    print(node, end=' ')
    for i in data[node]:
        if visit[i] == 0:
            dfs(i)

visit = [[0] * n]
from collections import deque
def bfs():
    q = deque()
    q.append(v)
    while q:
        i = q.popleft()
        print(i, end=' ')
        for node in data[i]:
            if visit[node] == 0:
                q.append(node)
                visit[node] = 1
