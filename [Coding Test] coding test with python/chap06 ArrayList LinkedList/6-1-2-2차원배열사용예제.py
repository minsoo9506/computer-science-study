# https://www.acmicpc.net/problem/2953

data = [list(map(int, input().split())) for _ in range(5)]

max_idx = 0
max_val = sum(data[0])
for idx, d in enumerate(data):
    if max_val < sum(d):
        max_val = sum(d)
        max_idx = idx

print(max_idx + 1, max_val)