# https://www.acmicpc.net/problem/16938

n, l, r, x = 5, 25, 35, 10
problem = [10,10,20,10,20]

from itertools import combinations

result = 0
for i in range(2, len(problem) + 1):
    candidates = list(combinations(problem, i))
    for c in candidates:
        if (sum(c) >= l) and (sum(c) <= r) and (max(c) - min(c) >= x):
            result += 1

print(result)