# https://www.acmicpc.net/problem/175

n = int(input())
data = list(map(int, input().split()))

import heapq

heapq.heapify(data)
answer = 0

while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    val_sum = a + b
    answer += val_sum
    heapq.heappush(data, val_sum)

print(answer)