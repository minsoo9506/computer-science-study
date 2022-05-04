# https://www.acmicpc.net/problem/1695

n = map(int, input())
a = list(map(int, input().split()))

b = a[::-1]

a = [0] + a
b = [0] + b
d = [[0] * (n + 1) for _ in range(n + 1)]
# d[i][j] = 수열 a의  i ~ j 에서 팰린드롬을 만들기 위해 필요한 최소 갯수

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i] == b[j]:
            d[i][j] = d[i + 1][j - 1]
        else:
            d[i][j] = min(d[i + 1][j], d[i][j - 1]) + 1

print(n - d[n][n])