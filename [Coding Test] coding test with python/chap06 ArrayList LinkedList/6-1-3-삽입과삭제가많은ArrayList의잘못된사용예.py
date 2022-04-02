# https://www.acmicpc.net/problem/2812

n, k = map(int, input().split())
data = list(input())

max_val = 0
from itertools import combinations
candidates = list(combinations(data, n - k))
for candidate in candidates:
    num = int(''.join(candidate))
    max_val = max(max_val, num)
print(max_val)