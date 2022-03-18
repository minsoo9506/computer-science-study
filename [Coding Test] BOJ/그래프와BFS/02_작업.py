# https://www.acmicpc.net/problem/2056

n = int(input())
work = [0] * (n + 1)
inDegree = [0] * (n + 1)
a = [[] for _ in range(n + 1)]
max_val = [0] * (n + 1) # 해당 작업이 완료되는 시간
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    work[i] = tmp[0]
    for x in tmp[2:]:
        a[x].append(i)
        inDegree[i] += 1

from collections import deque
q = deque()

for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)
        max_val[i] = work[i]

while q:
    x = q.popleft()
    for y in a[x]:
        inDegree[y] -= 1
        max_val[y] = max(max_val[y], max_val[x] + work[y])
        if inDegree[y] == 0:
            q.append(y)

print(max(max_val[1:]))