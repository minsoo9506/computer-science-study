# https://www.acmicpc.net/problem/10818

n = int(input())
data = list(map(int, input().split()))

max_val = data[0]
min_val = data[0]
for d in data[1:]:
    if d > max_val:
        max_val = d
    if d < min_val:
        min_val = d

print(min_val, max_val)