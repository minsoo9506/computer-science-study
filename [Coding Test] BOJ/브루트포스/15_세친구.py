# https://www.acmicpc.net/problem/17089

n, m = map(int, input().split())
friends = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
for _ in range(m):
    i, j = map(int, input().split())
    friends[i][j] = 1
    friends[j][i] = 1
    degree[i] += 1
    degree[j] += 1

ans = -1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if friends[i][j] == 1:
            for k in range(1, n + 1):
                if (friends[i][k] == 1) and (friends[j][k] == 1):
                    s = degree[i] + degree[j] + degree[k] - 6
                    ans = max(ans, s)
print(ans)