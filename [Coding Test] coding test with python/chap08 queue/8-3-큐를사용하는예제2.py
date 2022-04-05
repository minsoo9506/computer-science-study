# https://www.acmicpc.net/problem/2164

n = int(input())

from collections import deque

q = deque()
for i in range(1, n + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())