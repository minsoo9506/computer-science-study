# https://www.acmicpc.net/problem/3020
# 개똥벌레

n, h = map(int, input().split())
up = []
down = []
for i in range(n):
    x = int(input())
    if i % 2 == 0:
        down.append(x)
    else:
        up.append(x)

up.sort()
down.sort()

def find(start, end, target, data):
    while start < end:
        mid = (start + end) // 2
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

result = [0] * 500001
val = int(1e9)
answer = 0

for i in range(1, h + 1):
    idx_down = find(0, len(down), i, down)
    idx_up = find(0, len(up), i, up)
    result[i] = n // 2 - idx_down + n // 2 - idx_up
    val = min(val, result[i])
for i in range(1, h + 1):
    if result[i] == val:
        answer += 1
print(answer)