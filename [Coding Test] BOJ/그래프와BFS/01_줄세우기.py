# https://www.acmicpc.net/problem/2252
# 위상정렬

from collections import deque

q = deque()
n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    indegree[y] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=' ')
    for y in a[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)