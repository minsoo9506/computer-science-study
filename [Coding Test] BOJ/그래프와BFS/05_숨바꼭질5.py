# https://www.acmicpc.net/problem/17071

n, k = map(int, input().split())

# 수빈이 가능한 이동
# 2 * x, x - 1, x + 1
# 수빈이는 홀수초(or 짝수초)에 갈 수 있는 위치는 그 이후의 홀수초(or 짝수초)에도 무조건 갈 수 있다

from collections import deque
dist = [[-1] * 2 for _ in range(500000)] 
# dist[i][0] = i에 도착하는 가장 빠른 짝수시간
# dist[i][1] = i에 도착하는 가장 빠른 홀수시간
q = deque()
q.append((n, 0))
dist[n][0] = 0

while q:
     x, t = q.popleft()
     for y in [x - 1, x + 1, x * 2]:
         if 0 <= y <= 500000:
             if dist[y][1 - t] == -1: # 1 - t 로 홀짝 표현
                 dist[y][1 - t] = dist[x][t] + 1
                 q.append((y, 1 - t))
ans = -1
t = 0
while True:
    k += t # t초 후에 동생이 k에 있음
    if k > 500000:
        break
    if dist[k][t % 2] <= t:
        ans = t
        break
    t += 1
print(ans)