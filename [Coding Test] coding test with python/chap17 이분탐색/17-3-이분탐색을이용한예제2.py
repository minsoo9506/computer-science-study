# https://www.acmicpc.net/problem/1654
# 랜선 자르기

k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

start, end = 0, int(1e9)
result = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in data:
        tmp += i // mid
    if tmp >= n:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1