# https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())

# linked list 사용안함
from collections import deque
q = deque()

for i in range(1, n + 1):
    q.append(i)

while q:
    for _ in range(k - 1):
        num = q.popleft()
        q.append(num)
    out = q.popleft()
    print(out)